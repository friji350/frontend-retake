import { dev } from '$app/environment';

// we don't need any JS on this page, though we'll load
// it in dev so that we get hot module replacement
export const csr = dev;

// since there's no dynamic data here, we can prerender
// it so that it gets served as a static asset in production
export const prerender = true;

/** @type {import('./$types').PageLoad} */
export async function load() {
  try {

    const response = await fetch('http://127.0.0.1:8000/api/all_items');
    const data = await response.json();
    return {
      post: {
        titlePage: 'Admin',
        author: 'Anton Fadeenkov',
        des: 'Admin Page',
        itemCards: data,//TODO: переделать any
      },
    };
  } catch (error) {
    console.error('Ошибка при получении данных:', error);
  }
}


export async function _deleteItem({ id }: { id: number }) {
  try {
    const response = await fetch(`http://127.0.0.1:8000/api/all_items?id=${id}`, {
      method: 'DELETE',

    });

    if (!response.ok) {
      throw new Error('Ошибка при удалении элемента.');
    }


    console.log('Элемент успешно удален');
    window.location.reload();
  } catch (error) {
    console.error('Ошибка при удалении элемента:', error);
  }
}