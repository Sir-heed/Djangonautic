const titleInput = document.querySelector("input[name=title]");
const slugInput = document.querySelector("input[name=slug]");

const slugify = (val) => {
  return val
    .toString() // Conver to string
    .toLowerCase() // Convert to lowercase
    .trim() // Trim white spaces
    .replace(/&/g, "-and-") // replace & with -and-
    .replace(/[\s\W-]+/g, "-"); // replace spaces, non word chars and dashes with a single dash
};

titleInput.addEventListener("keyup", (e) => {
  slugInput.setAttribute("value", slugify(titleInput.value));
});
