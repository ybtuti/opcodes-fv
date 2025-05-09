// SPDX-License-Identifier: MIT
pragma solidity ^0.8.3;

import {Test, console2} from "forge-std/Test.sol";

contract Base_Test is Test {
    /*//////////////////////////////////////////////////////////////
                            HELPER FUNCTIONS
    //////////////////////////////////////////////////////////////*/

    // Based on uniswap
    function uniSqrt(uint256 y) internal pure returns (uint256 z) {
        if (y > 3) {
            z = y;
            uint256 x = y / 2 + 1;
            while (x < z) {
                z = x;
                x = (y / x + x) / 2;
            }
        } else if (y != 0) {
            z = 1;
        }
    }

    // Based on Solmate
    // https://github.com/transmissions11/solmate/blob/main/src/utils/FixedPointMathLib.sol
    function solmateSqrt(uint256 x) public pure returns (uint256 z) {
        assembly {
            z := shr(1, add(z, div(x, z)))
            z := shr(1, add(z, div(x, z)))
            z := shr(1, add(z, div(x, z)))
            z := shr(1, add(z, div(x, z)))
            z := shr(1, add(z, div(x, z)))
            z := shr(1, add(z, div(x, z)))
            z := shr(1, add(z, div(x, z)))

            z := sub(z, lt(div(x, z), z))
        }
    }
}
