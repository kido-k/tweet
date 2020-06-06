export const state = () => ({
  data: {}
})

export const mutations = {
  setData(state, data) {
    state.data = data
  }
}

export const actions = {
  async tweetAnalyze({ commit }, { url, param, config }) {
    await this.$axios
      .$post(url, param, config)
      .then(res => {
        commit('setData', res)
        localStorage.setItem('tweet', JSON.stringify(res))
      })
      .catch(e => {
        console.log(e)
      })
  }
}
