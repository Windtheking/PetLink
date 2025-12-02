
const mainHeader = document.getElementById('main-header');
const leftPanel = document.getElementById('left-panel');
const rightPanel = document.getElementById('right-panel');

// --- mover el header ---

const moveHeader = (headerClass) => {
    if (mainHeader) {
        mainHeader.classList.remove('header-left-active', 'header-right-active');
        
        mainHeader.classList.add(headerClass);
    }
};


const resetHeader = () => {
    if (mainHeader) {
        mainHeader.classList.remove('header-left-active', 'header-right-active');
    }
};




if (mainHeader && leftPanel && rightPanel) {
    
    
    leftPanel.addEventListener('mouseover', () => moveHeader('header-left-active'));
    leftPanel.addEventListener('mouseout', () => resetHeader());

    
    rightPanel.addEventListener('mouseover', () => moveHeader('header-right-active'));
    rightPanel.addEventListener('mouseout', () => resetHeader());
    
    console.log("Script de movimiento del header cargado y activo.");
}