// wallet.js - handles connecting to wallet, provider, signer, and contract instance
let provider, signer, contract;
let userAddress = null;
let contractOwnerAddress = null;

async function connectWallet() {
    if (!window.ethereum) {
        displayMessage("MetaMask or similar wallet not detected. Please install one.", 'error');
        return;
    }

    try {
        // Request account access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        userAddress = ethers.getAddress(accounts[0]);

        // Initialize Ethers provider and signer
        provider = new ethers.BrowserProvider(window.ethereum);
        signer = await provider.getSigner();

        // Initialize contract instance
        contract = new ethers.Contract(CONTRACT_ADDRESS, CONTRACT_ABI, signer);

        displayMessage("Wallet connected successfully!", 'success');
        await initializeDappState();

        // Set up event listeners for account/network changes
        window.ethereum.on('accountsChanged', (newAccounts) => {
            window.location.reload(); // Simple reload on account change
        });
        window.ethereum.on('chainChanged', () => {
            window.location.reload(); // Simple reload on network change
        });

    } catch (error) {
        console.error("Connection failed:", error);
        displayMessage("Could not connect wallet. User may have denied access.", 'error');
    }
}
