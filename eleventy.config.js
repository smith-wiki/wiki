const markdownIt = require("markdown-it");

module.exports = function (eleventyConfig) {
  eleventyConfig.addPassthroughCopy({ "wiki/assets": "assets" });
  eleventyConfig.addPassthroughCopy("CNAME");
  eleventyConfig.setLibrary(
    "md",
    markdownIt({ html: false, linkify: false, typographer: true }),
  );

  eleventyConfig.addFilter("machineDate", (value) => {
    const date = value instanceof Date ? value : new Date(value);
    return Number.isNaN(date.valueOf()) ? "" : date.toISOString();
  });

  eleventyConfig.addFilter("displayDate", (value) => {
    const date = value instanceof Date ? value : new Date(value);
    if (Number.isNaN(date.valueOf())) return "";
    return new Intl.DateTimeFormat("en", {
      year: "numeric",
      month: "short",
      day: "numeric",
      timeZone: "UTC",
    }).format(date);
  });

  return {
    dir: {
      input: "wiki",
      includes: "_includes",
      output: "_site",
    },
    htmlTemplateEngine: "njk",
    markdownTemplateEngine: false,
    templateFormats: ["md", "njk"],
  };
};
