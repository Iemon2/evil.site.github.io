function create_grid(album_grid, data) {
    for (const key in data) {
        album_grid.appendChild(create_album(key, data[key]));
    }
}

function create_album(name, data) {
    var album = document.createElement("div");
    album.setAttribute("class", "album");

    var title = document.createElement("h4");
    var image = document.createElement("img");
    var artist = document.createElement("h5");

    title.textContent = name;
    artist.textContent = data["Artist"];
    image.src = data["Cover"];
    image.alt = name + " album cover";

    album.appendChild(title);
    album.appendChild(image);
    album.appendChild(artist);

    return album
}

function readJSON(src) {
    fetch(src)
        .then(response => {
        if (!response.ok) {
            throw new Error('HTTP error! Status: ${response.status}');
        }
        return response.json();
        })
        .then(data => {
            create_grid(document.getElementById("album-grid"), data);
        })
        .catch(error => console.error('Failed to fetch data:', error));
}