#!/usr/bin/env python

import argparse
import copy
from datetime import date, datetime, timedelta
from operator import attrgetter
import os
from os import path
import re
import subprocess
import sys

from pybtex.database.input import bibtex as bibtex_in
from pybtex.database.output import bibtex as bibtex_out


#root = "/mounts/fsl3/disks/0/www/www-root/FSL"
svn_root = "https://subversion.cs.illinois.edu/svn/FSL"
www_root = "http://fslweb.cs.illinois.edu/FSL";


pdflatex_cmd = "/usr/local/texlive/2012/bin/x86_64-linux/pdflatex"
bibtex_cmd = "/usr/local/texlive/2012/bin/x86_64-linux/bibtex"
pdfheader_cmd = "/var/www/software/pdfheader/runner.sh"


# error/warning display helpers
silent_error_flag = False
def print_error(msg):
  sys.stderr.write("[error]: " + msg + "\n")
def print_warning(msg):
  sys.stderr.write("[warning]: " + msg + "\n")


# class for missing .bib field exception
class FieldError(Exception):
  def __init__(self, msg):
    self.msg = msg

  def __str__(self):
    return self.msg


# return .pdf file name for paper id 
pdf_ext = ".pdf"
def get_pdf(paper_id):
  return paper_id + pdf_ext

# return .tex file name for paper id 
tex_ext = ".tex"
def get_tex(paper_id):
  return paper_id + tex_ext

# return .bib file name for paper id 
bib_ext = ".bib"
def get_bib(paper_id):
  return paper_id + bib_ext

# return public .pdf file name for paper id 
def get_public_pdf(paper_id):
  return get_pdf(paper_id + "-public")

# return reviews file name for paper id 
def get_reviews(paper_id):
  return paper_id + "-reviews.txt"

bibtex2wiki_keys = ["abstract",
                    "project_url",
                    "project_name",
                    "author_id",
                    "category",
                    "hidden",
                    "to_appear",
                    # conference specific
                    "booktitle_acronym",
                    "booktitle_url",
                    "presentation",
                    # journal specific
                    "journal_acronym",
                    "journal_url"]


# bibtex parser and writer
writer = bibtex_out.Writer()


'''
Generic class containing the common fields for all papers: author, title,
abstract, project url (optional), project name (optional), author_id, and
category.
'''
class Paper(object):
  def __init__(self, id, year, entry):
    self.entry = entry

    # set id, author_id and category first, since they are used for
    # paper filtering
    self.id = id
 
    # set paper status
    if (id.endswith("draft")):
      self.status = "draft"
    elif (id.endswith("submission")):
      self.status = "submitted"
    else:
      self.status = "published"

    # set hidden
    self.hidden = self.type == "techreport" or self.status != "published"
    try:
      hidden_entry = entry.fields["hidden"]
      if (hidden_entry == "true"):
        self.hidden = True
      elif (hidden_entry == "false"): 
        self.hidden = False
    except KeyError: 
      pass

    # associate wiki names to authors
    self.add_list_field(entry, "author_id", "and")
       
    # parse the category list 
    self.add_list_field(entry, "category", ",")
    self.category = [category.lower() for category in self.category]

    # parse the fields common to conference papers, journal papers, and
    # technical reports
    try:
      self.author = entry.persons["author"]
    except KeyError: 
      raise FieldError("missing " + author + " field")
    if (len(self.author) != len(self.author_id)):
      err_msg = "<" + self.id + "> " + "item count mismatch: " \
              + str(len(self.author)) + " items in field " + "author" + " vs " \
              + str(len(self.author_id)) + " items in field " + "author_id"
      raise FieldError(err_msg)

    self.add_field(entry, "title")
    self.add_field(entry, "abstract")
    self.add_optional_field(entry, "project_url", warning=True)
    self.add_optional_field(entry, "project_name", default="project")

    # set date
    # set month
    try:
      mm = datetime.strptime(entry.fields["month"], "%B").month
    except ValueError:
      try:
        mm = datetime.strptime(entry.fields["month"], "%b").month
      except ValueError:
        #print_error("invalid month " + entry.fields["month"])
        print_warning("<" + self.id + "> " + "invalid month "
                      + entry.fields["month"] )
        mm = 1
    except KeyError:
      mm = 1

    # set year
    try:
      yyyy = int(entry.fields["year"][0:4])
    except ValueError:
      print_error("<" + self.id + "> " + "invalid year " + entry.fields["year"])
      yyyy = 1900
      print("===", self.get_id_year())
    except KeyError:
      yyyy = self.get_id_year()

    self.date = date(yyyy, mm, 1)

    # set to appear status
    try:
      to_appear_entry = entry.fields["to_appear"]
      if (to_appear_entry == "true"):
        self.to_appear = True
      elif (to_appear_entry == "false"): 
        self.to_appear = False
    except KeyError: 
      if (self.status == "published" and self.type != "techreport"
          and not isinstance(self, Thesis)):
        self.to_appear = not ("doi" in entry.fields or "pages" in entry.fields)
      else:
        self.to_appear = False

    # # set paper paths
    # self.paper_dir = path.join(path.join(args.papers, year), id)
    # self.presentation_dir = path.join(args.presentations, year)

  def add_field(self, entry, name):
    try:
      setattr(self, name, entry.fields[name])
    except KeyError:
      raise FieldError("<" + self.id + "> " + "missing " + name + " field")

  def add_optional_field(self, entry, name, default="", warning=False):
    flag = True
    try:
      value = entry.fields[name]
    except KeyError: 
      value = default
      flag = False
      if (warning):
        print_warning("<" + self.id + "> " + "missing " + name + " field")
    setattr(self, name, value)
    return flag

  def add_list_field(self, entry, name, sep):
    try:
      content = entry.fields[name]
    except KeyError: 
      raise FieldError("<" + self.id + "> " + "missing " + name + " field")

    if (sep != ""):
      if (sep[0].isalnum()):
        sep = "\s+" + sep
      else:
        sep = "\s*" + sep
      if (sep[-1].isalnum()):
        sep = sep + "\s+"
      else:
        sep = sep + "\s*"
    else:
      sep = "\s+"

    list = re.split(sep, content.strip())
    setattr(self, name, list)

  def get_title(self):
    return "name=" + self.title.replace("{", "").replace("}", "")

  def get_authors(self):
    #author_wikilink_list = ["[[" + id + "]]" for id in self.author_id]
    author_wikilink_list = [Paper.get_author_link(id) for id in self.author_id]
    authors = "authors=" + " and ".join(author_wikilink_list)

    return authors

  @staticmethod
  def get_author_link(id):
    if (id.startswith("http")):
      return "[" + id + "]"
    else:
      return "[[" + id + "]]"

  def get_abstract(self):
    return "abstract=" + self.abstract

  def get_wiki_content(self):
    if (self.hidden):
      return None

    wiki_content = "{{" + args.template \
                 + "|" + self.get_title() \
                 + "|" + self.get_authors() \
                 + "|" + self.get_details() \
                 + "|" + self.get_abstract() \
                 + "|" + self.get_links() \
                 + "}}"

    return wiki_content

  def get_details(self):
    details = "details=" + self.get_new() + " " + self.get_details_content()
    if (self.to_appear):
      details += ". To appear"

    return details

  @staticmethod
  def get_link_helper(url, name):
    if (url == None or url == ""):
      return None;
    else:
      return url + " " + name

  @staticmethod
  def get_links_helper(link_list):
    # filter the list of empty links (generated by optional fields)
    link_list = ["[" + link + "]" for link in link_list if link != None]
    links = "links=" + ", ".join(link_list)

    return links

  def get_pdf_link(self):
    return Paper.get_link_helper(self.public_pdf, "PDF")
 
  def get_project_link(self):
    return Paper.get_link_helper(self.project_url, self.project_name)

  def get_doi_link(self):
    doi = getattr(self, "doi", "")
    return Paper.get_link_helper(doi, "DOI")

  #def get_svn_link(self):
  #  if (args.private):
  #    svn = self.paper_svn
  #  else:
  #    svn = ""
  #  return Paper.get_link_helper(svn, "SVN")

  def get_reviews_link(self):
    if (args.private):
      reviews = self.reviews
    else:
      reviews = "" 
    return Paper.get_link_helper(reviews, "Reviews")

  def get_bib_link(self):
    return Paper.get_link_helper(self.bib, "BIB")

  def make_pdf(self):
    paper_tex = path.join(self.paper_dir, get_tex(self.id))
    # make paper_id.pdf only if paper_id.tex exists
    if (path.isfile(paper_tex)):
      #cmd = "echo $PATH"
      cmd = "cd " + self.paper_dir
      if (args.bibtex):
        cmd += " && " + pdflatex_cmd + " " + self.id \
             + " && " + bibtex_cmd + " " + self.id
      cmd += " && " + pdflatex_cmd + " " + self.id \
           + " && " + pdflatex_cmd + " " + self.id
      subprocess.call(cmd, shell=True)
    else:
      print_error("<" + self.id + "> " + "no such .tex file " + paper_tex)
      return

  def add_header(self):
    paper_pdf = path.join(self.paper_dir, get_pdf(self.id))
    # add header only if paper_id.pdf exists
    if (path.isfile(paper_pdf)):
      header = paper.get_details_content().replace("'''''", "")
      cmd = "cd " + self.paper_dir \
          + " && " + pdfheader_cmd \
          + " " + paper_pdf \
          + " \"" + header + "\"" \
          + " " + str(args.header_offset)
      subprocess.call(cmd, shell=True)
    else:
      print_error("<" + self.id + "> " + "no such .pdf file " + paper_pdf)
      return

    header_paper_pdf = path.join(self.paper_dir, get_pdf(paper_pdf + "-header"))
    public_paper_pdf = path.join(self.paper_dir, get_public_pdf(self.id))
    os.rename(header_paper_pdf, public_paper_pdf)

  def get_id_year(self):
    items = self.id.split("-")
    try:
      if (items[len(items) - 1] == "draft"
          or items[len(items) - 1] == "submission"):
        yyyy = items[len(items) - 3]
      else:
        yyyy = items[len(items) - 2]
 
      return int(yyyy)
    except:
      print_error("<" + self.id + "> " + "unexpected format of paper id ")
      return 1900

  def get_new(self):
    new_string = "NEWENTRY"
    # drafts and submissions are never new
    if (self.status != "published"):
      return ""
    # "to appear" papers are always new
    if (self.to_appear):
      return new_string
    # published papers are new 90 days after the publication month
    if (date.today() < self.date + timedelta(days=90)):
      return new_string
    else:
      return ""


'''
Class containing specific conference paper fields. Extends Paper.
'''
class ConferencePaper(Paper):
  type = "inproceedings"

  def __init__(self, id, year, entry):
    Paper.__init__(self, id, year, entry)
    
    if (self.status == "draft"):
      return

    # fields for submitted conference papers
    self.add_field(entry, "booktitle_acronym")
    self.add_optional_field(entry, "booktitle_url", warning=True)

    if (self.status == "submitted"):
      return

    # fields for conference papers accepted for publication
    self.add_field(entry, "booktitle")

    try:
      # series_acronym field supersedes publisher field
      # self.publisher = entry.fields["series"]
      self.publisher = entry.fields["series_acronym"]
    except KeyError: 
      try:
        # default to series field
        self.publisher = entry.fields["series"]
      except KeyError:
        try: 
          # default to publisher
          self.publisher = entry.fields["publisher"]
        except KeyError:
          # unknown publisher
          self.publisher = ""
          print_warning("<" + self.id + "> " + "missing "
                       + "publisher/series" + " field")
    # warning for unusual publisher/series
    # if (self.publisher != ""
    #    and self.publisher != "ACM"
    #    and self.publisher != "IEEE"
    #    and self.publisher != "LNCS"
    #    and self.publisher != "ENTCS"):
    #  print_warning("<" + self.id + "> " + "unrecognised publisher/series " 
    #                + self.publisher)
    self.add_optional_field(entry, "volume")
    # warning for LNCS/ENTCS with no volume info
    if (self.publisher == "LNCS" or self.publisher == "ENTCS"):
      if (self.volume == ""):
        print_warning("<" + self.id + "> "
                      + "missing volume information for LNCS/ENTCS publication")
    has_field = self.add_optional_field(entry, "pages", warning=True)
    #check the format of the content of pages
    if (has_field == True):
      if (self.pages != "---"):
        if (self.pages != ""):
          pattern = re.compile(r'([0-9]+)(\-)([0-9]+)')
          match = pattern.match(self.pages)
          if not match:
            print_warning("<" + self.id + "> " + "The format of pages \"" 
                        + self.pages + "\" is not correct")
        else:
          print_warning("<" + self.id +"> " + "missing pages content")
      else:
        self.pages = ""

    #self.add_field(entry, "month")
    self.add_optional_field(entry, "month", warning=True)

    self.add_field(entry, "year")

    self.add_optional_field(entry, "doi", warning=True)

    self.add_optional_field(entry, "presentation_url")
    if (self.presentation_url == ""):
      self.add_optional_field(entry, "presentation", warning=True)

  def get_details_content(self):
    details = ""
    if (self.status == "draft"):
      details += "draft"
      return details

    if (self.status == "submitted"):
      details += "submitted to " + self.booktitle_acronym
      return details

    details += "'''''" + self.booktitle_acronym + "'''''"
    if (self.publisher != ""):
      details += ", " + self.publisher
      if (self.volume != ""):
        details += " " + self.volume 
    if (self.pages != ""):
      details += ", " + "pp " + self.pages
    details += ". "
    details += self.year
   
    return details

  def get_links(self):
    link_list = []
    link_list.append(self.get_pdf_link())
    link_list.extend(self.get_presentation_links())
    link_list.append(self.get_project_link())
    link_list.append(self.get_doi_link())
    link_list.append(self.get_booktitle_link())
    #link_list.append(self.get_svn_link())
    link_list.append(self.get_reviews_link())
    link_list.append(self.get_bib_link())

    return Paper.get_links_helper(link_list) 

  def get_presentation_links(self):
    if (self.status != "published"):
      return []

    if (self.presentation_url != ""):
      return [Paper.get_link_helper(self.presentation_url, "Slides")]

    if (self.presentation == ""):
      return []

    prefix = path.join(self.presentation_dir, self.presentation)
    prefix_www = self.presentation_www + "/" + self.presentation

    presentation_links = [
        Paper.get_link_helper(
            prefix_www + "." + ext,
            "Slides(" + ext.upper() + ")")
        for ext in ["pptx", "ppt", "key", "pdf"]
        if path.isfile(prefix + "." + ext)]
    
    if (presentation_links == []):
      print_warning("<" + self.id + "> " + "no presentation found")

    return presentation_links

  def get_booktitle_link(self):
    try:
      return Paper.get_link_helper(self.booktitle_url, self.booktitle_acronym)
    except AttributeError:
      return None 


'''
Class containing specific journal paper fields. Extends Paper.
'''
class JournalPaper(Paper):
  type = "article"

  def __init__(self, id, year, entry):
    Paper.__init__(self, id, year, entry)

    if (self.status == "draft"):
      return

    # fields for submitted journal papers
    self.add_field(entry, "journal_acronym")
    self.add_field(entry, "journal_url")

    if (self.status == "submitted"):
      self.add_optional_field(entry, "year", warning=False)
      return

    # fields for journal papers accepted for publication
    self.add_field(entry, "journal")
    self.add_optional_field(entry, "volume", warning=True)
    self.add_optional_field(entry, "number", warning=True)
    has_field = self.add_optional_field(entry, "pages", warning=True)
    
    if (has_field == True):
      if (self.pages != "---"):
        if (self.pages != ""):
          pattern = re.compile(r'([0-9]+)(\-)([0-9]+)')
          match = pattern.match(self.pages)
          if not match:
            print_warning("<" + self.id + "> " + "The format of pages \""
                        + self.pages + "\" is not correct")
        else:
          print_warning("<" + self.id +"> " + "missing pages content")
      else:
        self.pages = ""


    self.add_optional_field(entry, "month", warning=True)
    self.add_field(entry, "year")
    self.add_optional_field(entry, "doi", warning=True)

  def get_details_content(self):
    details = ""

    #details for draft
    if (self.status == "draft"):
      details += "draft"
      return details

    #details for submitted
    if (self.status == "submitted"):
      details += "submitted to " + self.journal_acronym
      if (self.year != ""):
        details += ". " + self.year
      return details

    details += "'''''" + self.journal_acronym + "'''''"
    if (self.volume != ""):
      details += ", " + "Volume" + " " + self.volume 
    if (self.number != ""):
      details += "(" + self.number + ")"
    if (self.pages != ""):
      details += ", " + "pp " + self.pages
    details += ". " + self.year

    return details

  def get_links(self):
    link_list = []
    link_list.append(self.get_pdf_link())
    link_list.append(self.get_project_link())
    link_list.append(self.get_doi_link())
    link_list.append(self.get_journal_link())
    #link_list.append(self.get_svn_link())
    link_list.append(self.get_reviews_link())
    link_list.append(self.get_bib_link())

    return Paper.get_links_helper(link_list) 

  def get_journal_link(self):
    try:
      return Paper.get_link_helper(self.journal_url, self.journal_acronym)
    except AttributeError:
      return None 


'''
Class containing specific technical report fields. Extends Paper.
'''
class TechnicalReport(Paper):
  type = "techreport"

  def __init__(self, id, year, entry):
    Paper.__init__(self, id, year, entry)

    # the following case should not occur
    if (self.status != "published"):
      self.hidden = True
      return
      
    # fields for published technical reports
    self.add_field(entry, "institution")
    #self.add_field(entry, "month")
    self.add_optional_field(entry, "month", warning=True)
    self.add_field(entry, "year")
    self.add_field(entry, "number")
    self.add_optional_field(entry, "doi", default=self.number)

  def get_details_content(self):
    details = "'''''" + "Technical Report" + "'''''"

    # the following 3 cases should not occur
    if (self.status != "published"):
      return details

    details += " " + self.number + ", "
    details += self.month + " " + self.year
    return details

  def get_links(self):
    link_list = []
    link_list.append(self.get_pdf_link())
    link_list.append(self.get_project_link())
    link_list.append(self.get_doi_link())
    #link_list.append(self.get_svn_link())
    link_list.append(self.get_bib_link())

    return Paper.get_links_helper(link_list) 


'''
Class containing specific thesis fields. Extends Paper.
'''
class Thesis(Paper):

  def __init__(self, id, year, entry):
    Paper.__init__(self, id, year, entry)

    # the following case should not occur
    if (self.status != "published"):
      self.hidden = True
      return

    # fields for published technical reports
    self.add_field(entry, "school")
    #self.add_field(entry, "month")
    self.add_optional_field(entry, "month", warning=True)
    self.add_field(entry, "year")
    self.add_optional_field(entry, "doi", warning=True)

  def get_details_content(self):
    details = "'''''" + self.display_thesis_type + "'''''"

    # the following 3 cases should not occur
    if (self.status != "published"):
      return details

    details += ", " + self.school + ". "
    details += self.month + " " + self.year
    return details

  def get_links(self):
    link_list = []
    link_list.append(self.get_pdf_link())
    link_list.append(self.get_project_link())
    link_list.append(self.get_doi_link())
    #link_list.append(self.get_svn_link())
    link_list.append(self.get_bib_link())

    return Paper.get_links_helper(link_list)


'''
Class containing specific master thesis fields. Extends Thesis.
'''
class MasterThesis(Thesis):
  type = "mastersthesis"
  display_thesis_type = "Master's Thesis"

  def __init__(self, id, year, entry):
    Thesis.__init__(self, id, year, entry)


'''
Class containing specific phd thesis fields. Extends Thesis.
'''
class PhDThesis(Thesis):
  type = "phdthesis"
  display_thesis_type = "PhD Thesis"

  def __init__(self, id, year, entry):
    Thesis.__init__(self, id, year, entry)


'''
Helper functions.
'''
def get_bib_file(year_dir, paper_id):
  if (args.bibfile == None):
    paper_path = path.join(path.join(args.papers, year_dir), paper_id)
    bib_file = path.join(paper_path, get_bib(paper_id))
  else:
    bib_file = args.bibfile

  return bib_file

def parse_bib(bib_file):
  try:
    parser = bibtex_in.Parser()
    bib_data = parser.parse_file(bib_file)
  except Exception as e:
    print_error("cannot parse .bib file " + bib_file)
    print(e)
    return None

  return bib_data


def get_paper(bib_data, year_dir, paper_id):
  try:
    paper_entry = bib_data.entries[paper_id]
    if (paper_entry.type == ConferencePaper.type):
      paper = ConferencePaper(paper_id, year_dir, paper_entry) 
    elif (paper_entry.type == JournalPaper.type):
      paper = JournalPaper(paper_id, year_dir, paper_entry) 
    elif (paper_entry.type == TechnicalReport.type):
      paper = TechnicalReport(paper_id, year_dir, paper_entry) 
    elif (paper_entry.type == MasterThesis.type):
      paper = MasterThesis(paper_id, year_dir, paper_entry)
    elif (paper_entry.type == PhDThesis.type):
      paper = PhDThesis(paper_id, year_dir, paper_entry)
    else:
      print_error("<" + paper_id + "> " + "unsupported bib entry "
                  + paper_entry.type)
      return None
  except FieldError as e:
    print_error(str(e))
    return None

  return paper


def strip_bib(bib_data, year_dir, paper_id):
  stripped_bib_data = copy.deepcopy(bib_data)
  stripped_bib_data.entries[paper_id].fields = { 
      key: value 
      for key, value in bib_data.entries[paper_id].fields.items()
      if key not in bibtex2wiki_keys}

  try:
    paper_path = path.join(path.join(args.papers, year_dir), paper_id)
    stripped_bib_file = path.join(paper_path, get_bib(paper_id + "-ref"))
    file = open(stripped_bib_file, "w")
    writer.write_stream(stripped_bib_data, file)
    file.close()
  except IOError as e:
    print_error(str(e))


def get_paper_ids():
  if (args.ids != []):
    def filter(id):
      return id in args.ids
  else:
    def filter(id):
      return True

  paper_ids = [
      (dir, id)
      for dir in get_year_dirs()
        for id in os.listdir(path.join(args.papers, dir))
      if filter(id) and path.isdir(path.join(path.join(args.papers, dir), id))]

  return paper_ids

def get_year_dirs():
  if (args.years != []):
    def filter(year):
      return year.isdigit() and int(year) in args.years
  else:
    def filter(year):
      return year.isdigit()

  year_dirs = [
      dir
      for dir in os.listdir(args.papers)
      if filter(dir) and path.isdir(path.join(args.papers, dir))]

  year_dirs.sort(key=int, reverse=True)
  return year_dirs


args = None
### parse command line arguments
def parse_args():
  global args

  # common options for all actions
  common_parser = argparse.ArgumentParser(add_help=False)

  # generic options
  group = common_parser.add_mutually_exclusive_group()
  group.add_argument(
      "-s", "--silent",
      action="store_true",
      default=False,
      help="do not show warning/errors")
  group.add_argument(
      "-v", "--verbose",
      action="store_true",
      default=False,
      help="show warnings/errors")

  # paper filter options
  common_parser.add_argument(
      "--authors",
      nargs="*",
      default=[],
      help="only display papers by authors in the list",
      metavar=("author1", "author2"))
  common_parser.add_argument(
      "--categories",
      nargs="*",
      default=[],
      help="only display papers in categories in the list",
      metavar=("category1", "category2"))
  common_parser.add_argument(
      "--draft",
      action="store_true",
      default=False,
      help="display drafts, submission and technical reports")
  common_parser.add_argument(
      "--ids",
      nargs="*",
      default=[],
      help="only display papers with ids in the list",
      metavar=("id1", "id2"))
  common_parser.add_argument(
      "--years",
      nargs="*",
      default=[],
      type=int,
      help="only display papers from years in the list",
      metavar=("year1", "year2"))
  
  # location of source .bib file
  common_parser.add_argument(
      "--bibfile",
      help="use file instead of paper_id.bib",
      metavar="file")

  # main parser
  parser = argparse.ArgumentParser(
      description="",
      prog="bibtex2wiki")

  # action subparsers 
  subparsers = parser.add_subparsers(
      dest="action",
      title="actions",
      help="specify action (default wiki)")
  parser_bib = subparsers.add_parser(
      "bib",
      parents=[common_parser],
      help="generate stripped .bib file")
  parser_check = subparsers.add_parser(
      "check",
      parents=[common_parser],
      help="check .bib file consistency only")
  parser_header = subparsers.add_parser(
      "header",
      parents=[common_parser],
      help="add header to .pdf document")
  parser_pdf = subparsers.add_parser(
      "pdf",
      parents=[common_parser],
      help="generate .pdf document")
  parser_wiki = subparsers.add_parser(
      "wiki",
      parents=[common_parser],
      help="generate wiki template")

  # pdf subcommand options 
  parser_pdf.add_argument(
      "--bibtex",
      action="store_true",
      default=False,
      help="use bibtex to generate .bbl file")

  # header 
  parser_header.add_argument(
      "--header-offset",
      default=768,
      type=int,
      help="vertical header offset",
      metavar="offset")

  # wiki subcommand options 
  # display format options
  parser_wiki.add_argument(
      "--private",
      action="store_true",
      default=False,
      help="display private links")
  parser_wiki.add_argument(
      "--template",
      default="PubDefault",
      help="use wiki template")

  # url options
  parser_wiki.add_argument(
      "--svn",
      default=svn_root,
      help="URL of the FSL subversion repository",
      metavar="svn")
  parser_wiki.add_argument(
      "--www",
      default=www_root,
      help="URL of the FSL webpage",
      metavar="www")

  # root of the local repository
  parser.add_argument(
      "root",
      help="path to the local FSL subversion repository")


  # parse options
  args = parser.parse_args()

  # --private sets --draft
  if (args.action == "wiki"):
    args.draft = args.draft or args.private

  # convert categories to lowercase
  args.categories = [category.lower() for category in args.categories]

  # generate paths
  args.papers = path.join(args.root, "papers")
  args.presentations = path.join(args.root, "presentations")
  if (args.action == "wiki"):
    args.papers_svn = args.svn + "/papers"
    args.papers_www = args.www + "/papers"
    args.presentations_www = args.www + "/presentations"
  args.categories_file = path.join(args.papers, "fsl_categories.txt")


categories = []
### read categories from file
def get_categories():
  global categories

  try:
    file = open(args.categories_file, "r")
    categories = [
        line.strip().lower()
        for line in file
        if (line.strip() != "" and line.strip()[0] != "#")]
    file.close()
  except IOError as e:
    print_error(str(e))


if __name__ == "__main__":
  parse_args()

  get_categories()

  # chech that the args.categories
  for category in args.categories:
    if (not category in categories):
      print_error("category " + category + " not found in "
          + args.categories_file)

  paper_ids = get_paper_ids()
  if paper_ids == []:
    print_error("no papers selected")
    sys.exit(0)

  # list of papers (only for sorting wiki entries)
  papers = []

  for (year_dir, paper_id) in paper_ids:
    bib_file = get_bib_file(year_dir, paper_id)
    bib_data = parse_bib(bib_file)
    if (bib_data == None):
      continue

    if (paper_id not in bib_data.entries):
      print_error("no such bibtex entry " + paper_id + " in " + bib_file)
      continue

    if (args.action == "bib"):
      strip_bib(bib_data, year_dir, paper_id)
    else:
      paper = get_paper(bib_data, year_dir, paper_id)
      if (paper == None): 
        continue
      if (args.action == "check"):
        # errors/warning already displayed
        pass
      elif (args.action == "header"):
        paper.add_header()
      elif (args.action == "pdf"):
        # deprecated
        paper.make_pdf()
      elif (args.action == "wiki"):
        if (not paper.hidden):
          papers.append(paper)

  if (args.action == "wiki"):
    papers.sort(key=attrgetter("date"), reverse=True)
    for paper in papers:
      output = paper.get_wiki_content()
      if (output != None):
        print(output)

