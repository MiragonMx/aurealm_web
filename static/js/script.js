// select UI button
const btnLightDarkToggle = document.querySelector('.btn-light-dark-toggle');
// check OS theme preference
const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)");
// check local storage for OS overriding
const currentTheme = localStorage.getItem("theme");

// check if main logo necessary
const mainLogoImgDiv = document.querySelector("#img404, #imgHome");

// toggle theme after manual override
btnLightDarkToggle.addEventListener('click', () => {
  document.body.classList.toggle("light-theme");

  var theme = document.body.classList.contains("light-theme") ? "light" : "dark";
  localStorage.setItem("theme", theme);

  setThemeToggleBtnIcon();
});

// set button to reverse icon of current theme
function setThemeToggleBtnIcon() {
  let btnHtml = '';
  if (document.body.classList.contains('light-theme')) {
    btnHtml = '<svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" class="bi bi-moon" viewBox="0 0 16 16"> <path d="M6 .278a.768.768 0 0 1 .08.858 7.208 7.208 0 0 0-.878 3.46c0 4.021 3.278 7.277 7.318 7.277.527 0 1.04-.055 1.533-.16a.787.787 0 0 1 .81.316.733.733 0 0 1-.031.893A8.349 8.349 0 0 1 8.344 16C3.734 16 0 12.286 0 7.71 0 4.266 2.114 1.312 5.124.06A.752.752 0 0 1 6 .278zM4.858 1.311A7.269 7.269 0 0 0 1.025 7.71c0 4.02 3.279 7.276 7.319 7.276a7.316 7.316 0 0 0 5.205-2.162c-.337.042-.68.063-1.029.063-4.61 0-8.343-3.714-8.343-8.29 0-1.167.242-2.278.681-3.286z" /> </svg>'
    document.documentElement.removeAttribute('data-bs-theme');
  } else {
    btnHtml = ' <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" class="bi bi-sun" viewBox="0 0 16 16"> <path d="M8 11a3 3 0 1 1 0-6 3 3 0 0 1 0 6zm0 1a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM8 0a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 0zm0 13a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 13zm8-5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2a.5.5 0 0 1 .5.5zM3 8a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2A.5.5 0 0 1 3 8zm10.657-5.657a.5.5 0 0 1 0 .707l-1.414 1.415a.5.5 0 1 1-.707-.708l1.414-1.414a.5.5 0 0 1 .707 0zm-9.193 9.193a.5.5 0 0 1 0 .707L3.05 13.657a.5.5 0 0 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0zm9.193 2.121a.5.5 0 0 1-.707 0l-1.414-1.414a.5.5 0 0 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .707zM4.464 4.465a.5.5 0 0 1-.707 0L2.343 3.05a.5.5 0 1 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .708z" /> </svg>'
    document.documentElement.setAttribute('data-bs-theme', 'dark');
  }
  btnLightDarkToggle.innerHTML = btnHtml;

  if (null != mainLogoImgDiv) {
    let logoImgHtml = '';
    if (document.body.classList.contains('light-theme')) {
      logoImgHtml = ' <img src="/svg/full_logo_light_mode.svg" aria-hidden="true" focusable="false">'
    } else {
      logoImgHtml = ' <img src="/svg/full_logo_dark_mode.svg" aria-hidden="true" focusable="false">'
    }
    mainLogoImgDiv.lastElementChild.innerHTML = logoImgHtml;
  }
}

// set light theme, if OS preference or set in local storage (session)
if (currentTheme == "light") {// || !prefersDarkScheme.matches) {
  document.body.classList.add("light-theme");
}
// fill icon in general
setThemeToggleBtnIcon();
