/*
* Verification of GasBadNftMarketplace
*/

using GasBadNftMarketplace as gasBadNftMarketplace;
using NftMarketplace as nftMarketplace;

methods {
    function getListing(address nftAddress, uint256 tokenId) external returns (INftMarketplace.Listing) envfree;
    function getProceeds(address seller) external returns (uint256) envfree;
    // Use nftMock.safeTransferFrom for all safetransferFrom calls
    function _.safeTransferFrom(address,address,uint256) external => DISPATCHER(true);
    function _.onERC721Received(address,address,uint256,bytes) external => DISPATCHER(true);

}

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

rule calling_any_functon_should_result_in_each_contract_having_the_same_state(method f, method f2)

 {
    require(f.selector == f2.selector);
    // 1. call same function on NftMarketplace and Gas bad
    // 2. compare the getter functions to conclude that the contracts are still the same
    env e;
    calldataarg args;
    address listingAddr;
    uint256 tokenId;
    address seller;

    require(gasBadNftMarketplace.getProceeds(e, seller) == nftMarketplace.getProceeds(e, seller));
    require(gasBadNftMarketplace.getListing(e, listingAddr, tokenId).price == nftMarketplace.getListing(e, listingAddr, tokenId).price);
    require(gasBadNftMarketplace.getListing(e, listingAddr, tokenId).seller == nftMarketplace.getListing(e, listingAddr, tokenId).seller);


    // Act
    gasBadNftMarketplace.f(e, args);
    nftMarketplace.f2(e, args);

    // Assert
    assert(gasBadNftMarketplace.getProceeds(e, seller) == nftMarketplace.getProceeds(e, seller));
    assert(gasBadNftMarketplace.getListing(e,listingAddr, tokenId).price == nftMarketplace.getListing(e, listingAddr, tokenId).price);
    assert(gasBadNftMarketplace.getListing(e, listingAddr, tokenId).seller == nftMarketplace.getListing(e, listingAddr, tokenId).seller);
}