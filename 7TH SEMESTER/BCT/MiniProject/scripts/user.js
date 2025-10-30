// user.js - voter-facing functions

async function fetchCandidates() {
    if (!contract) return;
    
    const candidatesListVoter = el('candidates-list');
    const candidatesListAdmin = el('admin-candidates-list');
    candidatesListVoter.innerHTML = '';
    if (candidatesListAdmin) candidatesListAdmin.innerHTML = '';

    try {
        const count = Number(await contract.candidatesCount());
        
        for (let i = 1; i <= count; i++) {
            const candidate = await contract.candidates(i);
            const id = Number(candidate[0]);
            const name = candidate[1];
            const votes = Number(candidate[2]);

            // Render for Voter View
            candidatesListVoter.innerHTML += `
                <div class="card p-4 bg-indigo-50 border border-indigo-200 rounded-xl flex flex-col justify-between">
                    <div>
                        <h4 class="text-xl font-bold text-indigo-800">${name}</h4>
                        <p class="text-sm text-indigo-600 mb-4">Candidate ID: ${id}</p>
                    </div>
                    <button onclick="castVote(${id})" class="button-primary mt-3">
                        Vote for ${name}
                    </button>
                </div>
            `;

            // Render for Admin View (if present)
            if (candidatesListAdmin) {
                candidatesListAdmin.innerHTML += `
                    <div class="p-3 bg-red-100 border border-red-300 rounded-lg flex justify-between items-center">
                        <span class="text-red-800 font-semibold">${id}. ${name}</span>
                        <span class="text-red-600">Votes: ${votes}</span>
                    </div>
                `;
            }
        }
    } catch (error) {
        console.error("Error fetching candidates:", error);
        displayMessage("Could not load candidates. Ensure contract is deployed.", 'error');
    }
}

async function castVote(candidateId) {
    if (!signer) return displayMessage("Please connect your wallet first.", 'error');
    
    try {
        displayMessage(`Casting vote for candidate ID ${candidateId}...`, 'info');
        
        const tx = await contract.vote(candidateId);
        
        displayMessage("Transaction sent. Waiting for confirmation...", 'info');
        await tx.wait();
        
        displayMessage("Vote cast successfully! You cannot vote again.", 'success');
        
        // Hide voter view after successful vote
        el('voter-view').innerHTML = `
            <div class="p-6 bg-green-100 border border-green-300 rounded-xl text-center">
                <h2 class="text-3xl font-bold text-green-800 mb-4">Thank You!</h2>
                <p class="text-lg text-green-600">Your vote has been securely recorded on the blockchain.</p>
                <button onclick="showView('results-view'); fetchResults();" class="button-primary bg-green-600 hover:bg-green-700 mt-4">View Results</button>
            </div>
        `;
    } catch (error) {
        console.error("Voting failed:", error);
        displayMessage(error.reason || "Voting failed. Have you already voted?", 'error');
    }
}

async function fetchResults() {
    if (!contract) return;
    
    showView('results-view');
    const winnerDisplay = el('winner-display');
    const resultsList = el('results-candidates-list');
    resultsList.innerHTML = '<p class="text-center text-gray-500">Loading results...</p>';

    try {
        // 1. Get Winner
        const [winnerId, winnerName, winnerVotes] = await contract.getWinner();
        el('winner-name').textContent = winnerName.toString() === 'N/A' ? 'No Votes Yet' : winnerName;
        el('winner-votes').textContent = Number(winnerVotes);

        // 2. Get All Candidates and Render Table
        const count = Number(await contract.candidatesCount());
        resultsList.innerHTML = '';

        for (let i = 1; i <= count; i++) {
            const candidate = await contract.candidates(i);
            const id = Number(candidate[0]);
            const name = candidate[1];
            const votes = Number(candidate[2]);

            resultsList.innerHTML += `
                <div class="p-3 bg-gray-50 border border-gray-200 rounded-lg flex justify-between items-center">
                    <span class="text-gray-800 font-semibold">${id}. ${name}</span>
                    <span class="text-gray-600 font-bold">${votes} Votes</span>
                </div>
            `;
        }

    } catch (error) {
        console.error("Error fetching results:", error);
        displayMessage("Could not load election results.", 'error');
    }
}
