const fs = require("node:fs");

const KINDS = ["article", "book", "documentation", "paper", "repository", "specification", "video", "webpage"];
const DATE = /^\d{4}-\d{2}-\d{2}$/;
const TIMESTAMP = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$/;
const SHA256 = /^[0-9a-f]{64}$/;
const HTTP = /^https?:\/\/\S+$/;

function text(value) {
  return typeof value === "string" && value.trim() !== "";
}

function asString(value) {
  return value instanceof Date ? value.toISOString().replace(/\.000Z$/, "Z") : String(value ?? "");
}

function problems(data) {
  const found = [];
  for (const key of ["title", "summary", "author"]) {
    if (!text(data[key])) found.push(`${key} is empty`);
  }
  if (!HTTP.test(asString(data.url))) found.push("url must be an http(s) URL");
  if (!KINDS.includes(data.kind)) found.push(`kind must be one of ${KINDS.join(", ")}`);
  if (data.published !== undefined && !DATE.test(asString(data.published).slice(0, 10))) {
    found.push("published must be YYYY-MM-DD, or omitted when the source states no date");
  }
  if (!Array.isArray(data.captures) || data.captures.length === 0) {
    found.push("captures must list at least one capture");
  } else {
    data.captures.forEach((capture, index) => {
      if (!TIMESTAMP.test(asString(capture.retrieved))) found.push(`captures[${index}].retrieved must be YYYY-MM-DDTHH:MM:SSZ`);
      if (!SHA256.test(asString(capture.sha256))) found.push(`captures[${index}].sha256 must be 64 lowercase hex digits`);
      if (!text(capture.type)) found.push(`captures[${index}].type is empty`);
      if (capture.url !== undefined && !HTTP.test(asString(capture.url))) found.push(`captures[${index}].url must be an http(s) URL`);
    });
  }
  const body = fs.readFileSync(data.page.inputPath, "utf8").replace(/^---[\s\S]*?\n---/, "");
  for (const heading of ["## Overview", "## Key points"]) {
    if (!body.includes(`\n${heading}\n`)) found.push(`body needs a "${heading}" section`);
  }
  return found;
}

module.exports = {
  layout: "layouts/page.njk",
  eyebrow: "Source",
  tags: ["source"],
  templateEngineOverride: "md",
  eleventyComputed: {
    sourceChecked(data) {
      if (data.listTag) return false;
      const found = problems(data);
      if (found.length) {
        throw new Error(`Invalid source page ${data.page.inputPath}:\n- ${found.join("\n- ")}`);
      }
      return true;
    },
  },
};
