<script setup>
import { ref } from "vue";

defineProps({
  msg: String,
});

const count = ref(0);
</script>

<template>
  <div class="bg-gradient-to-tr from-indigo-500 via-purple-500 to-pink-500">
    <div class="flex justify-center h-screen">
      <div class="flex justify-center items-center w-full max-w-md px-6 mx-auto">
        <div class="flex-1">
          <div class="text-center">
            <h2
              class="
                text-4xl
                font-bold
                text-center text-gray-700
                dark:text-white
              "
            >
              Stori Challenge
            </h2>

            <p class="mt-3 text-gray-500 dark:text-gray-300">
              Sign in to access your account
              <br />
              <code> user: admin </code>
              <br />
              <code> password: tortadetamal123 </code>
            </p>
          </div>

          <div class="mt-8">
            <form>
              <div>
                <label
                  for="user"
                  class="block mb-2 text-sm text-gray-600 dark:text-gray-200"
                  >User</label
                >
                <input
                  type="user"
                  name="user"
                  id="user"
                  placeholder="RedPowerRanger"
                  class="
                    block
                    w-full
                    px-4
                    py-2
                    mt-2
                    text-gray-700
                    placeholder-gray-400
                    bg-white
                    border border-gray-200
                    rounded-md
                    dark:placeholder-gray-600
                    dark:bg-gray-900
                    dark:text-gray-300
                    dark:border-gray-700
                    focus:border-blue-400
                    dark:focus:border-blue-400
                    focus:ring-blue-400
                    focus:outline-none
                    focus:ring
                    focus:ring-opacity-40
                  "
                />
              </div>

              <div class="mt-6">
                <div class="flex justify-between mb-2">
                  <label
                    for="password"
                    class="text-sm text-gray-600 dark:text-gray-200"
                    >Password</label
                  >
                </div>

                <input
                  type="password"
                  name="password"
                  id="password"
                  placeholder="Your Password"
                  class="
                    block
                    w-full
                    px-4
                    py-2
                    mt-2
                    text-gray-700
                    placeholder-gray-400
                    bg-white
                    border border-gray-200
                    rounded-md
                    dark:placeholder-gray-600
                    dark:bg-gray-900
                    dark:text-gray-300
                    dark:border-gray-700
                    focus:border-blue-400
                    dark:focus:border-blue-400
                    focus:ring-blue-400
                    focus:outline-none
                    focus:ring
                    focus:ring-opacity-40
                  "
                />
              </div>

              <div class="mt-6">
                <a href="#/dashboard">
                  Login
                  <!-- <button
                  class="
                    bg-gradient-to-tr from-sky-500 to-fuchsia-300
                    w-full
                    px-4
                    py-2
                    tracking-wide
                    text-white
                    transition-colors
                    duration-200
                    transform
                    rounded-md
                    hover:bg-blue-400
                    focus:outline-none
                    focus:bg-blue-400
                    focus:ring
                    focus:ring-blue-300
                    focus:ring-opacity-50
                  "
                >
                  Sign in
                </button> -->
                </a>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
