/*
* Verification of MulwadUp for MathMasters
*/
methods {
    function mulWadUp(uint256 x, uint256 y) external returns uint256 envfree;
}

definition WAD() returns uint256 = 1000000000000000000;

rule check_testMulWadUpFuzz(uint256 x, uint256 y) {
    require(x == 0 || y == 0 || assert_uint256(y) <= assert_uint256(max_uint256 / x));
    uint256 result = mulWadUp(x, y);
    mathint expected = x * y == 0 ? 0 : (x * y - 1) / WAD() + 1;
    assert(result == expected);
    
}

// invariant check_testMulWadUpInvariant(uint256 x, uint256 y) 
//     mulWadUp(x, y) == assert_uint256(x * y == 0 ? 0 : (x * y - 1) / WAD() + 1)
//     {
//         preserved{
//             require(x == 0 || y == 0 || y <= assert_uint256(max_uint256 / x));
//         }
//     }
invariant check_testMulWadUpInvariant(uint256 x, uint256 y)
    mulWadUp(x, y) == assert_uint256(x * y == 0 ? 0 : (x * y - 1) / 1000000000000000000 + 1)
    {
        preserved {
            require (x == 0 || y == 0 || assert_uint256(y) <= assert_uint256(max_uint / x));
        }
    }