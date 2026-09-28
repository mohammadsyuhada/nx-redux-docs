const test = require("node:test");
const assert = require("node:assert");
const { counterpart, platformOf } = require("../docs/javascripts/platform-switch.js");

const pages = ["", "handheld/", "handheld/guide/context-menu/", "handheld/settings/led-control/",
  "mobile/", "mobile/library/", "reference/faq/"];

test("platformOf reads the first path segment", () => {
  assert.strictEqual(platformOf("handheld/guide/osd/"), "handheld");
  assert.strictEqual(platformOf("mobile/"), "mobile");
  assert.strictEqual(platformOf("reference/faq/"), null);
  assert.strictEqual(platformOf(""), null);
});

test("section overviews map to each other", () => {
  assert.strictEqual(counterpart("handheld/", pages), "mobile/");
  assert.strictEqual(counterpart("mobile/", pages), "handheld/");
});

test("a page with no match falls back to the other overview", () => {
  assert.strictEqual(counterpart("handheld/settings/led-control/", pages), "mobile/");
  assert.strictEqual(counterpart("mobile/library/", pages), "handheld/");
});

test("a matching page on the other side is used", () => {
  const withMatch = pages.concat(["mobile/guide/context-menu/"]);
  assert.strictEqual(counterpart("handheld/guide/context-menu/", withMatch), "mobile/guide/context-menu/");
});

test("an empty page list still returns the other overview", () => {
  assert.strictEqual(counterpart("handheld/guide/osd/", []), "mobile/");
});

test("pages outside a platform have no counterpart", () => {
  assert.strictEqual(counterpart("reference/faq/", pages), null);
});
