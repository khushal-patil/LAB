// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract Bank {
    // State variable
    address public accOwner;

    // Constructor - sets account owner
    constructor() {
        accOwner = msg.sender;
    }

    // Modifier to restrict access
    modifier onlyOwner() {
        require(msg.sender == accOwner, "You are not the account owner!");
        _;
    }

    // Deposit function
    function deposit() public payable onlyOwner {
        require(msg.value > 0, "Deposit amount must be greater than 0");
    }

    // Withdraw function
    function withdraw(uint256 amount) public onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than 0");
        require(amount <= address(this).balance, "Insufficient balance!");

        payable(msg.sender).transfer(amount);
    }

    // Show contract balance
    function showBalance() public view onlyOwner returns (uint256) {
        return address(this).balance;
    }

    // Fallback function to accept ether
    receive() external payable {}
    fallback() external payable {}
}
