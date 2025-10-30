// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract Voting {

    address public owner;

    // Struct to define a candidate
    struct Candidate {
        uint id;
        string name;
        uint voteCount;
    }

    // Mapping to store candidates by their ID
    mapping(uint => Candidate) public candidates;
    uint public candidatesCount;


    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this function.");
        _;
    }


    function addCandidate(string memory _name) public onlyOwner {
        candidatesCount++;
        candidates[candidatesCount] = Candidate(candidatesCount, _name, 0);
    }


    function registerVoter(address _voter) public onlyOwner {
        require(!isRegisteredVoter[_voter], "Voter is already registered.");
        isRegisteredVoter[_voter] = true;
    }


    function vote(uint _candidateId) public {
        // 1. Check if the sender is a registered voter
        require(isRegisteredVoter[msg.sender], "Error: Not a registered voter.");

        // 2. Check if the voter has already voted
        require(!voters[msg.sender], "Error: You have already voted.");

        // 3. Check if the candidate exists
        require(_candidateId > 0 && _candidateId <= candidatesCount, "Error: Invalid candidate ID.");

        // 4. Record that the voter has voted
        voters[msg.sender] = true;

        // 5. Increment the candidate's vote count
        candidates[_candidateId].voteCount++;
    }

    function checkIsRegistered(address _voter) public view returns (bool) {
        return isRegisteredVoter[_voter];
    }


    function getWinner() public view returns (uint winnerId, string memory winnerName, uint voteCount) {
        uint maxVotes = 0;
        uint currentWinnerId = 0;
        string memory currentWinnerName = "N/A";

        for (uint i = 1; i <= candidatesCount; i++) {
            if (candidates[i].voteCount > maxVotes) {
                maxVotes = candidates[i].voteCount;
                currentWinnerId = candidates[i].id;
                currentWinnerName = candidates[i].name;
            }
        }

        return (currentWinnerId, currentWinnerName, maxVotes);
    }
}
