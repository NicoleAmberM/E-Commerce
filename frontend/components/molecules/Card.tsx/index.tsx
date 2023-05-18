import Ratings from '@/components/atoms/Ratings'
import type { ProductType } from '@/utils/interface'
import Link from 'next/link'

interface CardProps {
	product: ProductType
}

const Card = ({ product }: CardProps): JSX.Element => {
	const { name, slug, category, categorySlug, description, price, ratings } =
		product
	return (
		<Link href={`/products/${categorySlug}/${slug}`} className=''>
			<div className='flex h-72  flex-col justify-start rounded-lg border overflow-hidden border-gray-300 bg-white gap-3'>
				<div className='flex flex-col gap-4'>
					<div className='h-36 bg-gray-300'></div>
					<div className='flex flex-1 flex-col gap-1.5 px-4 text-sm'>
						<div className='flex w-full flex-wrap justify-between items-center font-semibold'>
							{name}
							<div className='text-gray-400'>{`PHP ${parseFloat(
								price.toFixed(2)
							)}`}</div>
						</div>
						<div className='break-words line-clamp-3 text-xs text-justify'>
							{description}
						</div>
						<div className='flex justify-end'>
							<Ratings ratings={ratings} />
						</div>
					</div>
				</div>
			</div>
		</Link>
	)
}

export default Card
