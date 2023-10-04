// src/routes/item/[itemId].ts

import { dev } from '$app/environment';

export const csr = dev;
export const prerender = true;

/** @type {import('./$types').PageLoad} */
export async function load(page) {
  try {
    const id = page.url.searchParams.get('id');

    const response = await fetch(`http://127.0.0.1:8000/api/all_items?id=${id}`);
    const data = await response.json();
    return {
      post: {
        titlePage: data.name,
        author: 'Anton Fadeenkov',
        des: data.des,
        itemCard: data,
      },
    };
  } catch (error) {
    console.error('Ошибка при получении данных:', error);
  }
}
