const input_youtube_url = document.getElementById("youtube-url");
const btn_download = document.getElementById("btn-download");
const btn_link = document.getElementById("btn-auto-link");

function check_youtube_link(url) {
  if (url.match("https://www.youtube.com/")) {
    input_youtube_url.classList.remove("uk-form-danger");
    input_youtube_url.classList.add("uk-form-success");
    btn_download.disabled = false;
    btn_download.setAttribute("uk-tooltip", "YouMind로 동영상 다운로드");
    getYoutubeData(url);
  } else {
    input_youtube_url.classList.remove("uk-form-success");
    input_youtube_url.classList.add("uk-form-danger");
    btn_download.disabled = true;
    btn_download.setAttribute("uk-tooltip", "youtube 링크를 입력해 주세요");
  }
}
btn_download.onclick = e => {
  // window.open("file://C:/Windows/notepad.exe");
  chrome.extension
    .getBackgroundPage()
    .port.postMessage(input_youtube_url.value);
  input_youtube_url.value = "";
  check_youtube_link("");
};

btn_link.onclick = e => {
  chrome.tabs.getSelected(tab => {
    console.log(tab);
    const url = new URL(tab.url);
    input_youtube_url.value = url.href;
    check_youtube_link(url.href);
  });
};

function getYoutubeData(url) {
  const Url = new URL(url);
  const list = Url.searchParams.get("list");
  const id = Url.searchParams.get("v");
  let xhttp = new XMLHttpRequest();
  if (list) {
    xhttp.open(
      "GET",
      `https://www.googleapis.com/youtube/v3/playlistItems?key=AIzaSyCQ3RG5_ngnwRtP8cDfGDOdwhwHHE1Qcco&part=snippet&part=snippet&playlistId=${list}`,
      true
    );
  } else {
    xhttp.open(
      "GET",
      `https://www.googleapis.com/youtube/v3/videos?id=${id}&key=AIzaSyCQ3RG5_ngnwRtP8cDfGDOdwhwHHE1Qcco&part=snippet,contentDetails`,
      true
    );
  }
  xhttp.onreadystatechange = e => {
    if (xhttp.status === 200 && xhttp.readyState === 4) {
      console.log(JSON.parse(xhttp.responseText));
    }
  };
  xhttp.setRequestHeader("Content-Type", "application/json");
  xhttp.send();
}

// function getPlayList(list, token) {
//   let xhttp = new XMLHttpRequest();

// }

input_youtube_url.oninput = function(e) {
  const url = input_youtube_url.value;
  check_youtube_link(url);
};

chrome.tabs.getSelected(tab => {
  console.log(tab);
  const url = new URL(tab.url);
  if (url.origin === "https://www.youtube.com") {
    input_youtube_url.value = url.href;
  }
  check_youtube_link(url.href);
});
