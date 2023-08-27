// Yes ChatGPT did write this
// Function to read a cookie
function getCookie(name) {
    const cookieName = `${name}=`;
    const decodedCookie = decodeURIComponent(document.cookie);
    const cookieArray = decodedCookie.split(';');
    
    for (let i = 0; i < cookieArray.length; i++) {
      let cookie = cookieArray[i];
      while (cookie.charAt(0) === ' ') {
        cookie = cookie.substring(1);
      }
      if (cookie.indexOf(cookieName) === 0) {
        return cookie.substring(cookieName.length, cookie.length);
      }
    }
    
    return null;
}
  
// Function to set a new cookie
function setCookie(name, value, days) {
    const expirationDate = new Date();
    expirationDate.setTime(expirationDate.getTime() + (days * 24 * 60 * 60 * 1000));
    const expires = `expires=${expirationDate.toUTCString()}`;
    document.cookie = `${name}=${value};${expires};path=/`;
}

// Check if the cookie exists
const cookieName = 'joinAuto';
var existingCookie = getCookie(cookieName);

if (existingCookie === null) {
    setCookie(cookieName, '0', 365);
    existingCookie = '0'
}

// Load automatically if cookie is already on

const joinAutoSwitch = document.getElementById("joinauto")

if (existingCookie == "1") {
    window.location.href = "ROBLOXDEEPLINKPUTHERE"
    joinAutoSwitch.checked = true
}

// Change the cookie data if the user changes the switch
function updateSwitch() {
    if (joinAutoSwitch.checked) {
        setCookie(cookieName, '1', 365);
    } else {
        setCookie(cookieName, '0', 365)
    }
}
  
// Background movement
const bg1 = document.querySelector('.bg1');
const bg2 = document.querySelector('.bg2');

document.addEventListener('mousemove', (event) => {
    const mouseX = event.clientX;
    const mouseY = event.clientY;

    bg1.style.left = `${-mouseX/8 - 5}px`;
    bg1.style.top = `${-mouseY/8 - 5}px`;
    bg2.style.left = `${-mouseX/16 - 5}px`;
    bg2.style.top = `${-mouseY/16 - 5}px`;
});