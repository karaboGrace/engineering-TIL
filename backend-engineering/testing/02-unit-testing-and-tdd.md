# Unit Testing & Test-Driven Development (TDD)

## 1. Unit Testing
* **What it is:** Testing individual components in source code—such as classes and their methods—in isolation.
* **Design feedback:** Writing tests reveals whether a class or method follows the **single responsibility** guideline:
  * Too much responsibility $\rightarrow$ complex, painful tests.
  * Clear, focused responsibilities $\rightarrow$ straightforward tests.
* **Why structure matters:** Putting an entire application inside `Main` (or a single giant method) makes unit testing hard or nearly impossible. Splitting an app into small parts with clear responsibilities keeps code testable and maintainable.

---

## 2. Test-Driven Development (TDD)
TDD is an iterative development cycle where you write an automated test for a single piece of functionality **before** writing the production code that satisfies it.

### The TDD Loop (5 Steps)
1. **Write a test:** Pick a single behavior/functionality to test and write an automatically executable test for it.
2. **Run the test (expect failure):** Run the test suite to confirm the new test fails. Because the feature isn't implemented yet, a passing test here usually means the test itself is flawed or testing something that already exists.
3. **Write minimal functionality:** Implement just enough code to meet the test's requirements—add functionality in small increments rather than building extra unrequested features.
4. **Run the tests again:** Verify the test passes.
   * If tests **fail**, fix the implementation (or fix the test if the test logic itself was wrong).
5. **Refactor internal structure:** Clean up and reorganize code as the program grows—split overly long methods or isolate distinct concepts—without changing external behavior. Keep the existing tests unchanged so they act as a safety net: if refactoring accidentally breaks functionality, the tests will catch it.