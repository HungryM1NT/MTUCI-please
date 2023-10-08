authShow('form-login', 'form-register', 'switch-button')

initializePopup('login-popup', 'show-login-popup');

// add fields cleaning after closing

function authShow(loginId, registerId, buttonClass) {
    const buttons = document.getElementsByClassName(buttonClass)
    const login = document.getElementById(loginId)
    const register = document.getElementById(registerId)

    Array(...buttons).forEach(btn => {

        btn.addEventListener('click', () => {
            login.style.display = login.style.display === 'none' ? 'inline' : 'none'
            register.style.display = register.style.display === 'none' ? 'inline' : 'none'
        })
    })
}

function initializePopup(overlayId, popupShowButtonId, popupCancelButtonId=null) {
    const popupShowButton = document.getElementById(popupShowButtonId);
    if (!popupShowButton) return

    const popupOverlay = document.getElementById(overlayId);

    popupShowButton.addEventListener('click', () => {
        popupOverlay.style.display = 'flex';
    });

    popupOverlay.addEventListener('click', (event) => {
        if (event.target === popupOverlay) {
            popupOverlay.style.display = 'none';
        }
    });

    let popupCancelButton
    if (popupCancelButtonId) {
        popupCancelButton = document.getElementById(popupCancelButtonId)
        popupCancelButton.addEventListener('click', () => {
            popupOverlay.style.display = 'none';
        });
    }
}
