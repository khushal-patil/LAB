// admin.js - admin-facing functions

async function addCandidate() {
    if (!signer) return displayMessage("Please connect your wallet first.", 'error');
    
    const name = el('candidate-name').value;
    if (!name) return displayMessage("Candidate name cannot be empty.", 'error');

    try {
        displayMessage(`Submitting transaction for '${name}'...`, 'info');
        
        const tx = await contract.addCandidate(name);
        el('candidate-name').value = '';
        
        displayMessage("Transaction sent. Waiting for confirmation...", 'info');
        await tx.wait();
        
        displayMessage(`Candidate '${name}' added successfully!`, 'success');
        fetchCandidates(); // Refresh list
    } catch (error) {
        console.error("Add Candidate failed:", error);
        displayMessage(error.reason || "Failed to add candidate. Check if you are the owner.", 'error');
    }
}

async function registerVoter() {
    if (!signer) return displayMessage("Please connect your wallet first.", 'error');

    const address = el('voter-address').value;
    if (!ethers.isAddress(address)) return displayMessage("Invalid Ethereum address format.", 'error');

    try {
        displayMessage(`Submitting transaction to register ${address}...`, 'info');
        
        const tx = await contract.registerVoter(address);
        el('voter-address').value = '';
        
        displayMessage("Transaction sent. Waiting for confirmation...", 'info');
        await tx.wait();
        
        displayMessage(`Voter ${address.substring(0, 8)}... registered successfully!`, 'success');
    } catch (error) {
        console.error("Register Voter failed:", error);
        displayMessage(error.reason || "Failed to register voter. Check if you are the owner.", 'error');
    }
}
