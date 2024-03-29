import matter from 'gray-matter'
import marked from 'marked'
import yaml from 'js-yaml'

export async function getAllPosts() {
    const context = require.context('../_posts', false, /\.md$/)
    // const posts = []
    const posts = context.keys().map((key) => {
        const post = key.slice(2)
        const content = require(`../_posts/${post}`)
        const meta = matter(content.default)
        return {
            slug: post.replace('.md', ''),
            title: meta.data.title,
        }
    })

    return posts
}

export async function getPostBySlug(slug) {
    const fileContent = await import(`../_posts/${slug}.md`)
    const meta = matter(fileContent.default)
    const content = marked(meta.content)
    return {
        title: meta.data.title,
        content,
    }
}

export async function getConfig() {
    const config = await import('../config.yml')
    return yaml.safeLoad(config.default)
}
