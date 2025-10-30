// ui.js - UI helper functions and initialization

const el = (id) => document.getElementById(id);

function displayMessage(message, type = 'info') {
    const msgBox = el('message-box');
    msgBox.textContent = message;
    msgBox.className = 'p-4 rounded-lg text-center font-medium my-4'; // Reset classes
    msgBox.classList.add('block');

    if (type === 'success') {
        msgBox.classList.add('bg-green-100', 'text-green-800');
    } else if (type === 'error') {
        msgBox.classList.add('bg-red-100', 'text-red-800');
    } else {
        msgBox.classList.add('bg-blue-100', 'text-blue-800');
    }

    // Hide the message after 5 seconds
    setTimeout(() => {
        msgBox.classList.remove('block');
        msgBox.classList.add('hidden');
    }, 5000);
}

function showView(viewId) {
    el('voter-view').classList.add('hidden');
    el('admin-view').classList.add('hidden');
    el('results-view').classList.add('hidden');
    el('unregistered-view').classList.add('hidden');

    const view = el(viewId);
    if (view) {
        view.classList.remove('hidden');
    } else {
        console.error(`View ID not found: ${viewId}`);
    }
}

function toggleLoading(show) {
    if (show) {
        el('loading').classList.remove('hidden');
        el('voter-view').classList.add('hidden');
        el('admin-view').classList.add('hidden');
        el('unregistered-view').classList.add('hidden');
    } else {
        el('loading').classList.add('hidden');
    }
}

async function initializeDappState() {
    if (!contract || !userAddress) return;

    toggleLoading(true);

    el('account-address').textContent = userAddress.substring(0, 8) + '...';
    const network = await provider.getNetwork();
    el('network-id').textContent = network.name;
    
    try {
        // Fetch contract owner
        contractOwnerAddress = await contract.owner();
        const isOwner = userAddress.toLowerCase() === contractOwnerAddress.toLowerCase();
        el('user-role').textContent = isOwner ? 'Administrator' : 'Voter/Viewer';

        if (isOwner) {
            showView('admin-view');
            fetchCandidates(); // Initial fetch for admin
        } else {
            const isRegistered = await contract.checkIsRegistered(userAddress);

            if (isRegistered) {
                showView('voter-view');
                fetchCandidates(); // Initial fetch for voter
            } else {
                showView('unregistered-view');
            }
        }
    } catch (error) {
        console.error("Error fetching initial state:", error);
        displayMessage("Error reading contract data. Check console for details.", 'error');
    } finally {
        toggleLoading(false);
    }
}

window.onload = () => {
    // Try to auto-connect on load. The button is still available for manual connection.
    const connectButton = el('connect-wallet');
    if (connectButton) connectButton.click();
};
