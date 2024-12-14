---
title: Home
layout: page
---

# Image Recognizer

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  </head>
  <body>
    <input type="file" class="form-control" id="photo" accept="image/*" />
    <br /><br />
    <img
      id="preview"
      src=""
      alt="Selected Image Preview"
      style="max-width: 300px; display: none"
    />
  <!-- <script>
    <label class="input-group-text" for="inputGroupFile02">Upload</label> -->
    <!-- <div id="results"></div> -->
    <!-- <script>
    const photo = document.getElementById("photo");
    const result = document.getElementById("results");
    async function loaded(reader) {
      const response = await fetch(
        "https://sakibice007-fruits-recognization-2.hf.space/--replicas/p6lru/predict",
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ data: [reader.result] }),
        }
      );
      const json = await response.json();
      const label = json["data"][0]["label"];
      result.innerHTML = `<br/> <img src = "${reader.result}" width="450" height="200"> <p>${label}</p>`;
    }
    function read() {
      const reader = new FileReader();
      reader.addEventListener("load", () => loaded(reader));
      reader.readAsDataURL(photo.files[0]);
    }
    photo.addEventListener("input", read);
  </script> -->

  <script type="module">
    const photoInput = document.getElementById("photo");
      const preview = document.getElementById("preview");

      photoInput.addEventListener("change", function (event) {
        const file = event.target.files[0]; // Get the selected file
        if (file) {
          const reader = new FileReader();

          // Load the image as a base64 URL
          reader.onload = function (e) {
            preview.src = e.target.result; // Set the image src
            preview.style.display = "block"; // Make the image visible
          };

          reader.readAsDataURL(file); // Read the file
        } else {
          preview.src = ""; // Clear the preview if no file is selected
          preview.style.display = "none"; // Hide the image
        }
      });
    import { client } from "https://cdn.jsdelivr.net/npm/@gradio/client/dist/index.min.js";
    async function loaded(reader) {
      const app = await client(
        "https://sakibice007-fruits-recognization-2.hf.space/--replicas/p6lru/"
      );
      const response = await app.predict("/predict", [reader.result]);

      // const json = await response.json();
      // const label = json["data"][0]["label"];
      const label = response["data"][0]["label"];
      results.innerHTML = `<br/> <img src = "${reader.result}" width="500"> <p>${label}</p>`;
    }
    function read() {
      const reader = new FileReader();
      reader.addEventListener("load", () => loaded(reader));
      reader.readAsDataURL(photo.files[0]);
    }
    photo.addEventListener("input", read);

    console.log(result.data);
  
  </script>
  </body>
</html>
Can classify 20 different types of Fruits <br/>
The types are following: <br/>

1. Mangoes
2. Apples
3. Pineapples
4. Oranges
5. Papaya
6. Watermelon
7. Muskmelon
8. Blackberry
9. Litchi
10. Grapes
11. Kiwi
12. Plums
13. Peaches
14. Strawberries
15. Tomato
16. Cherry
17. Bael
18. Cucumber
19. Mulberry
20. Ice Apple
