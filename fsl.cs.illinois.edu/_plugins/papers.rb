require 'pathname'
require 'bibtex'
require "i18n"
require "ostruct"

I18n.config.available_locales = :en

module Papers
  class Generator < Jekyll::Generator
    def generate(site)
      site.data['papers'] = []
      site.data['papers_ids'].each do |path|
        path = Pathname.new(path)
        paper = PaperPage.new(site, path)
        site.pages << paper
        site.data['papers'] << paper
      end
      site.data['papers'] = site.data['papers'].sort_by{|paper| paper['date']}.reverse
    end
  end

  class PaperPage < Jekyll::Page
    def initialize(site, path)
      @site = site
      @base = site.source
      @dir  = path.dirname.to_s

      @basename = path.basename.to_s 
      @ext      = '.md'
      @name     = @basename + @ext

      bib = BibTeX.open(Pathname.new('../..') / path / (@basename + '.bib')).convert(:latex)
      bibentry  = bib[self.basename]
      
      @data = {
        'category' => 'paper',
        'layout' => 'paper'
      }
      @data['bib'] = { }
      @data['title'] = @data['bib']['title'] = bibentry.title
      @data['date']  = @data['bib']['date']  = bibentry.date
      @data['bib']['abstract'] = bibentry.abstract
      @data['bib']['authors'] = bibentry.author
      
      @data['bib']['publisher']         = defined?(bibentry['publisher'])         ? bibentry['publisher']         : nil
      @data['bib']['booktitle']         = defined?(bibentry['booktitle'])         ? bibentry['booktitle']         : nil
      @data['bib']['booktitle_acronym'] = defined?(bibentry['booktitle_acronym']) ? bibentry['booktitle_acronym'] : nil
      @data['bib']['booktitle_url']     = defined?(bibentry['booktitle_url'])     ? bibentry['booktitle_url']     : nil
     
      @data['bib']['numpages']         = defined?(bibentry['numpages'])         ? bibentry['numpages']         : nil
      @data['bib']['pages']         = defined?(bibentry['pages'])         ? bibentry['pages']         : nil
      
      @data['bib']['project']           = defined?(bibentry['project'])     ? bibentry['project']      : nil
      @data['bib']['project_url']       = defined?(bibentry['project_url']) ? bibentry['project_url']  : nil
      @data['bib']['number']            = defined?(bibentry['number'])      ? bibentry['number']       : nil
      author_links = []
      bibentry.author.each { |author| author_links << makelink(author) }
      @data['bib']['author_links'] = author_links
      @content = ""

      Jekyll::Hooks.trigger :pages, :post_init, self
    end
    
    def makelink(author)
        # TODO: It's probably better to do this in a template
        if author.first and author.last then
            first = I18n.transliterate(author.first).to_s.downcase
            last = I18n.transliterate(author.last).to_s.downcase
            return '<a href="../../people/' + first + '-' + last + '">' + author.to_s + '</a>'
        else
            return author.to_s
        end
    end
  end
end

