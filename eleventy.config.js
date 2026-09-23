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

  eleventyConfig.addFilter("byTitle", (items) =>
    [...items].sort((a, b) => String(a.data.title).localeCompare(String(b.data.title))),
  );

  eleventyConfig.addFilter("groupByDay", (items) => {
    const days = new Map();
    for (const item of [...items].reverse()) {
      const day = item.date.toISOString().slice(0, 10);
      if (!days.has(day)) days.set(day, []);
      days.get(day).push(item);
    }
    return [...days].map(([day, dayItems]) => ({ day, items: dayItems }));
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
