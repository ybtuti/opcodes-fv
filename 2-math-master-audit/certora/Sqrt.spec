/*
* Verification of MulwadUp for MathMasters
*/

methods {
    // function mathMastersSqrt(uint256) external returns uint256 envfree;
    // function uniSqrt(uint256) external returns uint256 envfree;
    function mathMastersTopHalf(uint256) external returns uint256 envfree;
    function solmateTopHalf(uint256) external returns uint256 envfree;
}

rule solMateTopHalfMatchesMathMastersTopHalfSqrt(uint256 x) {
    assert(mathMastersTopHalf(x) == solmateTopHalf(x));
}

// rule uniSqrtMatchesMathMastersSqrt(uint256 x) {
//     assert(mathMastersSqrt(x) == uniSqrt(x));
// }