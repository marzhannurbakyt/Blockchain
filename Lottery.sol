pragma solidity ^0.5.16;

contract Lottery {

    address public manager;
    address payable[] public players;

    constructor() public {
        manager = msg.sender;
    }

    function enter() public payable {
        require(msg.value > 1 ether);

        players.push(msg.sender);
    }

    function random() private view returns (uint) {
        return uint(keccak256(abi.encodePacked(now, msg.sender, this)));
    }

    function pickWinner() public payable {
        uint index = random() % players.length;
        players[index].transfer(address(this).balance);
        players = new address payable[](0);
    }

    function getPlayers() public view returns (address payable[] memory) {
        return players;
    }
    
    function resetLottery() internal {
        players = new address payable[](0);
    }

} 
