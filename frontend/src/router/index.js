import { createRouter, createWebHistory } from 'vue-router'
import MemeList from '../views/MemeList.vue'
import MemeDetail from '../views/MemeDetail.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', name: 'home', component: MemeList},
        { path: '/meme/:id', name: 'meme-detail', component: MemeDetail}
    ]
})

export default router