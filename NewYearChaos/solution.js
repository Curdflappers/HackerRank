'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
  inputString += inputStdin;
});

process.stdin.on('end', _ => {
  inputString = inputString.replace(/\s*$/, '')
    .split('\n')
    .map(str => str.replace(/\s*$/, ''));

  main();
});

function readLine() {
  return inputString[currentLine++];
}

// Complete the minimumBribes function below.
// Use console.log to write to stdout, write 'Too chaotic' for impossible queues
function minimumBribes(q) {
  let bribes = 0;
  let tree = initFenwickTree(q.length);
  for (let i = q.length - 1; i >= 0; i--) {
    if (q[i] > i + 3) { // 0-based index means 2 skips + 1 index = 3 difference
      return 'Too chaotic';
    } else {
      let current = q[i];
      bribes += queryFenwickTree(tree, current - 1);
      updateFenwickTree(tree, current - 1, 1);
    }
  }
  return bribes;
}

function runTests() {
  const PASS = 'SUCCESS'; // flag value
  let passed = true, actual, expected;

  // Too chaotic
  actual = minimumBribes([4, 1, 2, 3]);
  expected = 'Too chaotic';
  passed = test(actual, expected) && passed; // test first to evaluate it

  // No changes
  actual = minimumBribes([1, 2, 3, 4]);
  expected = 0;
  passed = test(actual, expected) && passed;

  // Lots of changes
  actual = minimumBribes([1, 2, 5, 3, 4, 7, 8, 6]);
  expected = 4;
  passed = test(actual, expected) && passed;

  // Print message and return
  if (passed) {
    console.log('SUCCESS: All tests passed');
  }
  else {
    console.log('FAILURE: See messages above');
  }
  return passed;


  /**
   * Expects actual and expected to be exactly equal.
   * 
   * If equal, returns true
   * If not, prints error message and returns false
   */
  function test(actual, expected) {
    if (actual !== expected) {
      console.log(`Expected '${actual}' to be '${expected}'`);
      return false;
    }
    return true;
  }
}

//////////////////
// FENWICK TREE //
//////////////////
/**
 * Modified from https://raw.githubusercontent.com/mikolalysenko/fenwick-tree/master/fenwick.js
 */

/**
 * Returns a new tree of all 0's
 */
function initFenwickTree(length) {
  // Fastest algorithm from https://jsperf.com/zeroarrayjs
  let out = new Array(length);
  let i = length;
  while (--i >= 0) {
    out[i] = 0;
  }
  return out;
}

function updateFenwickTree(tree, at, by) {
  var n = tree.length;
  at |= 0;
  while (at < n) {
    tree[at] += by;
    at |= (at + 1);
  }
}

function queryFenwickTree(tree, at) {
  var res = 0;
  at |= 0;
  while (at >= 0) {
    res += tree[at];
    at = (at & (at + 1)) - 1;
  }
  return res;
}

function main() {
  // don't execute production code if test code fails
  /* Test block
  let testsPassed = runTests();
  if(!testsPassed) return;
  //*/ // End test block

  const t = parseInt(readLine(), 10);

  for (let tItr = 0; tItr < t; tItr++) {
    const n = parseInt(readLine(), 10);

    const q = readLine().split(' ').map(qTemp => parseInt(qTemp, 10));

    console.log(minimumBribes(q));
  }
}
