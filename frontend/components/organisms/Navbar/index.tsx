import { HiShoppingBag, HiUserCircle } from 'react-icons/hi2'

import SearchInput from '@/components/atoms/Search'
import Link from 'next/link'
import { useState } from 'react'
import { RiCake3Line } from 'react-icons/ri'

// import { HiOutlineSearch } from 'react-icons/hi'

const Navbar = (): JSX.Element => {
	const [searchTerm, setSearchTerm] = useState('')

	const onSearchChange = (value: string): void => {
		setSearchTerm(value)
	}

	return (
		<nav className='sticky top-0 z-10 h-16 w-full border border-gray-200 bg-white drop-shadow-md'>
			<div className='flex h-full flex-wrap justify-between items-center gap-2 px-8'>
				<div className='flex items-center gap-4'>
					<Link href='/' className='mr-4'>
						<div className='items-center text-blue-700'>
							<RiCake3Line className='text-xl' />
						</div>
					</Link>
					{/* <SearchInput
					value={searchTerm}
					onChange={(e) => onSearchChange(e.target.value)}
				/> */}
					<Link
						href='/'
						className='text-sm text-gray-800 font-medium hover:text-blue-700'>
						Cakes
					</Link>
					<Link
						href='/'
						className='text-sm text-gray-800 font-medium hover:text-blue-700'>
						Pastries
					</Link>
					<Link
						href='/'
						className='text-sm text-gray-800 font-medium hover:text-blue-700'>
						Cookies
					</Link>
					<Link
						href='/'
						className='text-sm text-gray-800 font-medium hover:text-blue-700'>
						Loaves & Bars
					</Link>
				</div>
				<div className='flex items-center gap-3'>
					{/* <HiOutlineSearch
						title='Search'
						className='text-2xl text-gray-600 hover:text-blue-700'
					/> */}
					<SearchInput
						value={searchTerm}
						onChange={(e) => onSearchChange(e.target.value)}
					/>
					<HiShoppingBag
						title='My Cart'
						className='text-2xl text-gray-700 hover:text-blue-700'
					/>
					<HiUserCircle
						title='My Profile'
						className='text-2xl text-gray-700 hover:text-blue-700'
					/>
				</div>
			</div>
		</nav>
	)
}

export default Navbar
