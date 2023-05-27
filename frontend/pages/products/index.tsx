import Card from '@/components/molecules/Card.tsx'
import { useGetProductsQuery } from '@/services/productSlice'
import { ProductType } from '@/utils/types'

const ProductList = (): JSX.Element => {
	const { data: products = [], isLoading, error } = useGetProductsQuery()

	if (isLoading) {
		return (
			<div className='flex h-screen justify-center items-center'>
				Loading...
			</div>
		)
	}

	return (
		<div className='flex flex-col gap-4 overflow-y-auto'>
			<div className='h-80 bg-gray-300 rounded-md'></div>
			<div className='grid w-full grid-cols-1 sm:grid-cols-2 md:grid-cols-3 xl:grid-cols-5 gap-4 content-center'>
				{products.map((product: ProductType): JSX.Element => {
					return <Card key={product.id} product={product}></Card>
				})}
			</div>
		</div>
	)
}

export default ProductList
