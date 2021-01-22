module Jekyll
  class PaperInfoTag < Liquid::Tag

    def initialize(tag_name, text, tokens)
      super
      @text = text
    end

    # convert string s to hyperlink at url
    def makelink(url, s)
      '<a href="' + url + '">' + s + '</a>'
    end
    
    def render(context)
      id = "#{context[@text.strip]}"
      site = context.registers[:site]
      curr = site.collections["papers"].docs.find { |paper| paper.id == id }
      out = ""
      # display authors, hyperlinked to author page
      curr["authors"].each { |author|
        out += makelink("../people/" + author.gsub(" ", "-"), author) + " and "
      }
      out = out[0..-6] # remove trailing and
      out += ", " + curr["date"].to_s()[0..3] # display year
      out
    end

  end
end

Liquid::Template.register_tag('paper_info', Jekyll::PaperInfoTag)
