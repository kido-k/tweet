<template>
  <v-app>
    <v-content class="wrap">
      <v-container>
        <nuxt />
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
export default {
  data() {
    return {}
  }
}
</script>

<style scoped>
.wrap {
  background: linear-gradient(to right, #fff, #00e676);
}
</style>
