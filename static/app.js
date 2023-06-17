const DEFUALT_URL = "http://127.0.0.1:5000//api";

/**Creates html data about cupcakes. */
function createCupcakeHTML(cupcake) {
    return `
      <div data-cupcake-id=${cupcake.id}>
        <li>
          Flavor: ${cupcake.flavor} | Size: ${cupcake.size} | Rating: ${cupcake.rating}
        </li>
        <img class="cupcake-img" src="${cupcake.image}" alt="(no image was given)">
        <br>
        <button class="delete-btn">Delete</button>
      </div>
    `;
  }

/**Displays existing cupcakes on page. */
  async function showCupcakes() {
    const res = await axios.get(`${DEFUALT_URL}/cupcakes`);
  
    for (let cupcake of res.data.cupcakes) {
      let newCupcake = $(createCupcakeHTML(cupcake));

      $("#all-cupcakes").append(newCupcake);
    }
  }

/**Handles adding of new cupcakes. */
  $("#new-cupcake").on("submit", async function (e) {
    e.preventDefault();
  
    let flavor = $("#flavor").val();
    let size = $("#size").val();
    let rating = $("#rating").val();
    let image = $("#image").val();
  
    const newCupcakeRes = await axios.post(`${DEFUALT_URL}/cupcakes`, {
      flavor,
      size,
      rating,
      image
    });
  
    let newCupcake = $(createCupcakeHTML(newCupcakeRes.data.cupcake));

    $("#all-cupcakes").append(newCupcake);
    $("#new-cupcake").trigger("reset");
  });

/**Handles deleting of cupcakes. */
  $("#all-cupcakes").on("click", ".delete-btn", async function (e) {
    e.preventDefault();
    
    let $cupcake = $(e.target).closest("div");
    let $id = $cupcake.attr("data-cupcake-id");
  
    await axios.delete(`${DEFUALT_URL}/cupcakes/${$id}`);
    $cupcake.remove();
  });
  
  $(showCupcakes);