import Card from '@/components/molecules/Card.tsx'
import type { ProductType } from '@/utils/interface'

const products: ProductType[] = [
	{
		id: 1,
		name: 'Blueberry Cheesecake',
		slug: 'blueberry-cheesecake',
		category: 'Cakes',
		categorySlug: 'cakes',
		price: 450.0,
		description:
			'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua',
		ratings: [
			{
				score: 3,
			},
		],
	},
	{
		id: 2,
		name: 'Banana Loaf',
		slug: 'banana-loaf',
		category: 'Bars',
		categorySlug: 'bars',
		price: 250.0,
		description:
			'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua',
		ratings: [
			{
				score: 5,
			},
		],
	},
	{
		id: 3,
		name: 'Food for the Gods',
		slug: 'food-for-the-gods',
		category: 'Bars',
		categorySlug: 'bars',
		price: 500.0,
		description:
			'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua',
		ratings: [
			{
				score: 5,
			},
		],
	},
	{
		id: 4,
		name: 'Oatmeal Cookies',
		slug: 'oatmeal-cookies',
		category: 'Cookies',
		categorySlug: 'cookies',
		price: 200.0,
		description:
			'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua',
		ratings: [
			{
				score: 4,
			},
		],
	},
	{
		id: 5,
		name: 'Sans Rival Cake',
		slug: 'sans-rival-cake',
		category: 'Cakes',
		categorySlug: 'cakes',
		price: 800.156,
		description:
			'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua',
		ratings: [
			{
				score: 5,
			},
		],
	},
]

const ProductList = (): JSX.Element => {
	return (
		<div className='flex flex-col gap-4 overflow-y-auto'>
			<div className='h-80 bg-gray-300 rounded-md'></div>
			<div className='grid w-full grid-cols-1 sm:grid-cols-2 md:grid-cols-3 xl:grid-cols-5 gap-4 content-center'>
				{products.map((product): JSX.Element => {
					return <Card key={product.id} product={product}></Card>
				})}
			</div>
		</div>
	)
}

export default ProductList
