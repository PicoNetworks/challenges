import Link from 'next/link'
import { getConfig, getAllPosts } from '../api'
import DefaultLayout from '../_layouts/default'

export default function Blog(props) {
    return (
        <DefaultLayout title={props.title} description={props.description}>
            <p>List of posts:</p>
            <ul>
                {props.posts.map((post) => (
                    <li key={post.title}>
                        <Link href={`/posts/${post.slug}`}>
                            <a>{post.title}</a>
                        </Link>
                    </li>
                ))}
            </ul>
        </DefaultLayout>
    )
}

export async function getStaticProps() {
    const config = await getConfig()
    const allPosts = await getAllPosts()

    return {
        props: {
            posts: allPosts,
            title: config.title,
            description: config.description,
        },
    }
}
