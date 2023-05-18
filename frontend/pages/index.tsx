import Layout from '@/components/layout'
import Navbar from '@/components/organisms/Navbar'
import ProductList from './products'

export default function Home() {
	return (
		<>
			<Layout pageTitle='Home'>
				<div className='flex flex-col'>
					<Navbar />
					<div className='p-4'>
						<ProductList />
					</div>
				</div>
			</Layout>
		</>
	)
}
