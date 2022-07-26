<script setup>
import { ref } from "vue";

defineProps({
  msg: String,
});

const count = ref(0);

</script>

<template>
  <div class="bg-gradient-to-tr from-indigo-500 via-purple-500 to-pink-500 text-center">
    <h1 class="tracking-wide text-4xl text-gray-900 pt-20 font-bold">Dashboard</h1>
    <section
      id="addRecipients"
      class="p-4 flex flex-col justify-center min-h-screen max-w-md mx-auto"
    >
      <div class="p-6 bg-sky-100 rounded">
        <div class="flex items-center justify-center font-black m-3 mb-12">
          <svg
            class="h-10 w-10 mr-3 text-purple-600 animate-pulse"
            viewBox="0 0 20 20"
            fill="currentColor"
          >
            <path
              fill="currentColor"
              d="M5.177,17.658c0,0,3.445,1.987,4.823,1.987c2.067,0,4.823-1.987,4.823-1.987c0.024-0.025,0.044-0.054,0.068-0.08H5.109C5.133,17.604,5.153,17.633,5.177,17.658z M8.622,1.583V0.531C6.496,0.973,2.539,2.521,1.376,7.933H0.699c-0.189,0-0.344,0.155-0.344,0.344v1.378C0.354,9.845,0.509,10,0.699,10h0.392c-0.016,0.224-0.026,0.454-0.033,0.689H0.699c-0.189,0-0.344,0.155-0.344,0.344v1.378c0,0.189,0.155,0.344,0.344,0.344h0.439c0.089,0.79,0.262,1.804,0.594,2.849v2.663H4.34c-2.233-2.449-2.264-6.822-2.264-7.01C2.077,4.052,6.353,2.108,8.622,1.583zM10.689,0.354H9.311v2.059h1.378V0.354z M11.378,2.63v0.472H8.622V2.63C6.612,3.147,3.11,4.951,3.11,11.258c0,0,0.004,3.373,1.47,5.632h4.042v-0.689h2.756v0.689h4.042c1.466-2.259,1.47-5.632,1.47-5.632C16.89,4.951,13.388,3.147,11.378,2.63z M5.005,12.035c-0.318-0.364-0.517-0.833-0.517-1.354S4.687,9.69,5.005,9.327V12.035zM6.383,10.026c-0.295,0.078-0.517,0.335-0.517,0.654c0,0.319,0.222,0.576,0.517,0.654v1.395c-0.384-0.032-0.738-0.163-1.033-0.377V9.008c0.296-0.214,0.649-0.345,1.033-0.377V10.026z M7.761,12.353c-0.296,0.214-0.649,0.345-1.033,0.377v-1.395C7.022,11.257,7.244,11,7.244,10.681c0-0.319-0.222-0.576-0.517-0.654V8.631c0.384,0.032,0.738,0.163,1.033,0.377V12.353zM8.105,12.035V9.327c0.318,0.363,0.517,0.833,0.517,1.354S8.423,11.671,8.105,12.035z M10,13.445l-1.378,0.689L10,12.756l1.378,1.378L10,13.445z M11.895,12.035c-0.318-0.364-0.517-0.833-0.517-1.354s0.199-0.991,0.517-1.354V12.035z M13.273,10.026c-0.295,0.078-0.517,0.335-0.517,0.654c0,0.319,0.222,0.576,0.517,0.654v1.395c-0.384-0.032-0.738-0.163-1.033-0.377V9.008c0.296-0.214,0.649-0.345,1.033-0.377V10.026z M14.651,12.353c-0.296,0.214-0.649,0.345-1.033,0.377v-1.395c0.295-0.078,0.517-0.335,0.517-0.654c0-0.319-0.222-0.576-0.517-0.654V8.631c0.384,0.032,0.738,0.163,1.033,0.377V12.353zM14.995,12.035V9.327c0.318,0.363,0.517,0.833,0.517,1.354S15.313,11.671,14.995,12.035z M19.646,9.656V8.278c0-0.189-0.155-0.344-0.344-0.344h-0.678c-1.163-5.413-5.12-6.96-7.246-7.402v1.052c2.269,0.525,6.545,2.469,6.545,9.675c0,0.188-0.031,4.561-2.264,7.01h2.608v-2.663c0.333-1.044,0.505-2.058,0.594-2.849h0.439c0.189,0,0.344-0.155,0.344-0.344v-1.378c0-0.189-0.155-0.344-0.344-0.344h-0.359c-0.007-0.235-0.017-0.465-0.033-0.689h0.392C19.491,10,19.646,9.845,19.646,9.656z"
            ></path>
          </svg>
          <h1 class="tracking-wide text-3xl text-gray-900">Add Recipients</h1>
        </div>
        <form
          id="login_form"
          action="api_login"
          method="POST"
          class="flex flex-col justify-center"
        >
          <label class="text-sm font-medium text-gray-900">Name</label>
          <input
            class="
              mb-3
              px-2
              py-1.5
              mb-3
              mt-1
              block
              w-full
              px-2
              py-1.5
              border border-gray-300
              rounded-md
              text-sm
              shadow-sm
              placeholder-gray-400
              focus:outline-none
              focus:border-sky-500
              focus:ring-1
              focus:ring-sky-500
              focus:invalid:border-red-500
              focus:invalid:ring-red-500
            "
            type="text"
            name="name"
            placeholder="Jacobo"
          />
          <label class="text-sm font-medium text-gray-900">Email</label>
          <input
            class="
              mb-3
              px-2
              py-1.5
              mb-3
              mt-1
              block
              w-full
              px-2
              py-1.5
              border border-gray-300
              rounded-md
              text-sm
              shadow-sm
              placeholder-gray-400
              focus:outline-none
              focus:border-sky-500
              focus:ring-1
              focus:ring-sky-500
              focus:invalid:border-red-500
              focus:invalid:ring-red-500
            "
            type="email"
            name="email"
            placeholder="jacobo@email.com"
          />
          <button
            class="
              px-4
              py-1.5
              rounded-md
              shadow-lg
              bg-gradient-to-r
              from-pink-600
              to-red-600
              font-medium
              text-gray-100
              block
              transition
              duration-300
            "
            type="submit"
          >
            <span id="login_process_state" class="hidden">Sending :)</span>
            <span id="login_default_state"
              >Add recipient<span id="subtotal"></span
            ></span>
          </button>
        </form>
      </div>
    </section>

    <section
      id="uploadAsset"
      class="p-4 flex flex-col justify-center min-h-screen max-w-md mx-auto"
    >
      <div class="p-6 bg-sky-100 rounded">
        <div class="flex items-center justify-center font-black m-3 mb-12">
          <svg
            class="h-10 w-10 mr-3 text-red-600 animate-pulse"
            viewBox="0 0 20 20"
          >
            <path
              fill="currentColor"
              d="M19.68,0.345c-0.218-0.232-0.583-0.243-0.814-0.025L8.645,9.932l1.968,0.844l9.066-9.641C19.886,0.915,19.89,0.568,19.68,0.345z"
            ></path>
            <polygon
              points="8.858,13.626 10.845,11.639 7.368,10.149 6.374,11.142 6.126,10.894 5.629,11.391 5.877,11.639 4.883,12.632 7.368,15.117 8.361,14.123 8.609,14.371 9.106,13.874"
            ></polygon>
            <rect
              x="2.545"
              y="12.657"
              transform="matrix(0.7072 0.7071 -0.7071 0.7072 11.5364 2.3789)"
              width="0.703"
              height="4.918"
            ></rect>
            <rect
              x="3.539"
              y="13.651"
              transform="matrix(0.7071 0.7072 -0.7072 0.7071 12.5319 1.9686)"
              width="0.703"
              height="4.918"
            ></rect>
            <rect
              x="4.532"
              y="14.645"
              transform="matrix(-0.7071 -0.7071 0.7071 -0.7071 -3.7574 32.6509)"
              width="0.703"
              height="4.918"
            ></rect>
            <rect
              x="0.001"
              y="18.243"
              transform="matrix(-0.7071 -0.7071 0.7071 -0.7071 -10.748 32.7361)"
              width="2.81"
              height="0.703"
            ></rect>
          </svg>
          <h1 class="tracking-wide text-3xl text-gray-900">Upload assets</h1>
        </div>
        <form
          id="login_form"
          action="api_login"
          method="POST"
          class="flex flex-col justify-center"
        >
          <label class="text-sm font-medium text-gray-900">Asset</label>
          <input
            class="
              mb-3
              px-2
              py-1.5
              mb-3
              mt-1
              block
              w-full
              px-2
              py-1.5
              border border-gray-300
              rounded-md
              text-sm
              shadow-sm
              placeholder-gray-400
              focus:outline-none
              focus:border-sky-500
              focus:ring-1
              focus:ring-sky-500
              focus:invalid:border-red-500
              focus:invalid:ring-red-500
            "
            type="text"
            name="assetName"
            placeholder="Newsletter 1 asset"
          />
          
          <label class="text-sm font-medium text-gray-900"
            >File</label
          >
          <input
            class="
              mb-3
              mt-1
              block
              w-full
              px-2
              py-1.5
              border border-gray-300
              rounded-md
              text-sm
              shadow-sm
              placeholder-gray-400
              focus:outline-none
              focus:border-sky-500
              focus:ring-1
              focus:ring-sky-500
              focus:invalid:border-red-500
              focus:invalid:ring-red-500
            "
            name="assetFile"
            type="file" accept="image/*,.pdf"
          />
          <button
            class="
              px-4
              py-1.5
              rounded-md
              shadow-lg
              bg-gradient-to-r
              from-pink-600
              to-red-600
              font-medium
              text-gray-100
              block
              transition
              duration-300
            "
            type="submit"
          >
            <span id="login_process_state" class="hidden">Sending :)</span>
            <span id="login_default_state"
              >Upload<span id="subtotal"></span
            ></span>
          </button>
        </form>
      </div>
    </section>

    <section
      id="sendNewsletter"
      class="p-4 flex flex-col justify-center min-h-screen max-w-md mx-auto"
    >
      <div class="p-6 bg-sky-100 rounded">
        <div class="flex items-center justify-center font-black m-3 mb-12">
          <svg
            class="h-10 w-10 mr-3 text-purple-600 animate-pulse"
            viewBox="0 0 20 20"
          >
            <path
              fill="currentColor"
              d="M7.83,3.404l1.741-2.909C9.367,0.407,9.15,0.344,8.913,0.344c-0.954,0-1.728,0.774-1.728,1.728C7.185,2.613,7.441,3.087,7.83,3.404z"
            ></path>
            <path
              fill="currentColor"
              d="M19.645,12.002l-0.464-0.31c-0.09-1.505-0.628-2.972-1.575-4.187l-1.212,0.156l0.084-0.125c0.316-0.473,0.188-1.119-0.286-1.435L15.517,5.65c-0.473-0.316-1.119-0.187-1.435,0.286l-0.095,0.142l-0.538-3.219l-3.271-2.033l-1.754,2.93l0.86,0.481L3.04,3.445L2.136,4.798l3.766,2.516c-0.17,0.204-0.333,0.414-0.484,0.639C5.269,8.178,5.137,8.41,5.013,8.645L1.247,6.129L0.344,7.482l4.878,8.537l0.008-0.013c0.098,0.164,0.207,0.322,0.317,0.479l1.628-0.209l-0.302,0.452c-0.316,0.473-0.187,1.119,0.286,1.435l0.675,0.451c0.473,0.316,1.119,0.188,1.435-0.286l0.252-0.378l0.185,1.442c1.418,0.385,2.904,0.334,4.273-0.105l0.552,0.369c1.512-0.533,2.87-1.542,3.829-2.977C19.32,15.244,19.732,13.602,19.645,12.002z M14.09,16.055c-0.106,0.158-0.32,0.201-0.478,0.095c-0.158-0.106-0.201-0.32-0.095-0.478c0.106-0.158,0.32-0.201,0.478-0.095C14.153,15.682,14.196,15.896,14.09,16.055zM13.969,13.664c-0.513,0.769-1.371,1.227-2.296,1.227c-0.546,0-1.075-0.161-1.531-0.465c-1.265-0.845-1.606-2.561-0.762-3.826c0.513-0.768,1.372-1.227,2.297-1.227c0.545,0,1.074,0.161,1.53,0.465C14.472,10.683,14.814,12.4,13.969,13.664z M15.065,17.476c-0.106,0.158-0.32,0.201-0.478,0.095c-0.158-0.106-0.201-0.32-0.095-0.478c0.106-0.158,0.32-0.201,0.478-0.095C15.129,17.104,15.171,17.318,15.065,17.476z M15.334,14.768c-0.106,0.158-0.32,0.201-0.478,0.095c-0.158-0.106-0.201-0.32-0.095-0.478c0.106-0.158,0.32-0.201,0.478-0.095C15.397,14.396,15.44,14.61,15.334,14.768zM15.568,13.222c-0.158-0.106-0.201-0.32-0.095-0.478c0.106-0.158,0.32-0.201,0.478-0.095c0.158,0.106,0.201,0.32,0.095,0.478C15.94,13.285,15.726,13.327,15.568,13.222z M16.665,15.658c-0.106,0.158-0.32,0.201-0.478,0.095c-0.158-0.106-0.201-0.32-0.095-0.478c0.106-0.158,0.32-0.201,0.478-0.095S16.771,15.499,16.665,15.658z M17.733,13.483c-0.106,0.158-0.32,0.201-0.478,0.095c-0.158-0.106-0.201-0.32-0.095-0.478c0.106-0.158,0.32-0.201,0.478-0.095C17.796,13.111,17.839,13.325,17.733,13.483z"
            ></path>
            <path
              fill="currentColor"
              d="M12.824,10.412c-0.341-0.228-0.738-0.349-1.146-0.349c-0.694,0-1.338,0.344-1.723,0.92c-0.634,0.949-0.377,2.236,0.571,2.869c0.342,0.228,0.739,0.35,1.147,0.35c0.694,0,1.337-0.344,1.722-0.92C14.029,12.332,13.773,11.045,12.824,10.412z"
            ></path>
          </svg>
          <h1 class="tracking-wide text-3xl text-gray-900">
            Create Newsletter
          </h1>
        </div>
        <form
          id="login_form"
          action="api_login"
          method="POST"
          class="flex flex-col justify-center"
        >
          <label class="text-sm font-medium text-gray-900">Name</label>
          <input
            class="
              mb-3
              px-2
              py-1.5
              mb-3
              mt-1
              block
              w-full
              px-2
              py-1.5
              border border-gray-300
              rounded-md
              text-sm
              shadow-sm
              placeholder-gray-400
              focus:outline-none
              focus:border-sky-500
              focus:ring-1
              focus:ring-sky-500
              focus:invalid:border-red-500
              focus:invalid:ring-red-500
            "
            type="text"
            name="newsletterName"
            placeholder="My new newsletter"
          />
          <label class="text-sm font-medium text-gray-900">Content</label>
          <textarea
            class="
              mb-3
              mt-1
              block
              w-full
              px-2
              py-1.5
              border border-gray-300
              rounded-md
              text-sm
              shadow-sm
              placeholder-gray-400
              focus:outline-none
              focus:border-sky-500
              focus:ring-1
              focus:ring-sky-500
              focus:invalid:border-red-500
              focus:invalid:ring-red-500
            "
            name="messages"
            placeholder="Write something"
          ></textarea>
          <label class="text-sm font-medium text-gray-900"
            >Attachment</label
          >
          <select
            class="
              mb-3
              px-2
              py-1.5
              mb-3
              mt-1
              block
              w-full
              px-2
              py-1.5
              border border-gray-300
              rounded-md
              text-sm
              shadow-sm
              placeholder-gray-400
              focus:outline-none
              focus:border-sky-500
              focus:ring-1
              focus:ring-sky-500
              focus:invalid:border-red-500
              focus:invalid:ring-red-500
            "
            name="newsletterAttachment"
          >
            <option value="newsletter1">newsletter 1</option>
          </select>

          <button
            class="
              px-4
              py-1.5
              rounded-md
              shadow-lg
              bg-gradient-to-r
              from-pink-600
              to-red-600
              font-medium
              text-gray-100
              block
              transition
              duration-300
            "
            type="submit"
          >
            <span id="login_process_state" class="hidden">Sending :)</span>
            <span id="login_default_state"
              >Create<span id="subtotal"></span
            ></span>
          </button>
        </form>
      </div>
    </section>
  </div>
</template>

<style scoped>
</style>
