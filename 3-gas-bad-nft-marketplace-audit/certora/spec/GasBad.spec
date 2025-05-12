/*
* Verification of GasBadNftMarketplace
*/

ghost mathint listingUpdatesCount {
    init_state axiom listingUpdatesCount == 0;
    // initial state will be 0
    // require this to be true
}
ghost mathint log4Count {
    init_state axiom log4Count == 0;
    // initial state will be 0
    // require this to be true
}
// TODO: Make this conribution, link to docs: https://docs.certora.com/en/latest/docs/prover/changelog/prover_changelog.html#march-15-2024
hook Sstore s_listings[KEY address nftAddress][KEY uint256 tokenId].price uint256 price /*STORAGE*/ {
    listingUpdatesCount = listingUpdatesCount + 1;
}

hook LOG4(uint offset, uint length, bytes32 t1, bytes32 t2, bytes32 t3, bytes32 t4) {
    log4Count = log4Count + 1;
}

/*//////////////////////////////////////////////////////////////
                            RULES
//////////////////////////////////////////////////////////////*/

invariant anytime_mapping_updated_emit_event() 
    listingUpdatesCount <= log4Count;
