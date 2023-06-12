export interface RoleType {
  id: number
  name: string
}

export interface UserType {
  id: number
  role: RoleType
  slug: string
  first_name: string
  last_name: string
  email: string
  contactNumber: string
  address: string
}

export interface CategoryType {
	id: number
	name: string
	slug: string
}

export interface ProductType {
	id: number
	category: CategoryType
	name: string
	slug: string
	description: string
	price: number
  ratings: number
}

export interface RatingType {
  // id: number
  // product: ProductType
  // customer: UserType
  score: number
  // review: string
  // createdAt: string
}