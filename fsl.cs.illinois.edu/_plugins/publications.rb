module Jekyll
  class CategoryPageGenerator < Generator
    safe true

    def generate(site)
    end
  end
end

module FormalSystemsLab
    Publication = Struct.new(:name, :path, :title, :authors, :abstract, :status)
end
