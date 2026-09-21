const RKEY_PATTERN = /^[a-z0-9._~:-]{1,512}$/i;

module.exports = {
  layout: "layouts/research.njk",
  tags: ["research"],
  templateEngineOverride: "md",
  eleventyComputed: {
    permalink(data) {
      const rkey = String(data.rkey || "");
      if (!RKEY_PATTERN.test(rkey) || rkey === "." || rkey === "..") {
        throw new Error(`Research page has an invalid rkey: ${rkey || "<missing>"}`);
      }
      return `/research/${rkey}/index.html`;
    },
  },
};
