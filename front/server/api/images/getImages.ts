type MyApiResponse = { message: string }[]

export default defineEventHandler(async (event) => {
    const data = await $fetch<MyApiResponse>('http://fast_api:8000')
    console.log(data[0].message)
    return data 
})