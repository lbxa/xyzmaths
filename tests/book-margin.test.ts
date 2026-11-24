import assert from "node:assert/strict";
import { test } from "node:test";
import { marginOffsets } from "../src/lib/book-margin";

test("margin entries start at their references when there is room", () => {
  assert.deepEqual(marginOffsets([], 10), []);
  assert.deepEqual(marginOffsets([{ top: 40, height: 20 }, { top: 160, height: 15 }], 10), [40, 90]);
});

test("crowded notes stack in order and later entries recover their own alignment", () => {
  const entries = [
    { top: 12, height: 48 }, { top: 20, height: 22 },
    { top: 20, height: 18 }, { top: 170, height: 5 },
  ];
  assert.deepEqual(marginOffsets(entries, 6), [12, 0, 0, 52]);
});
