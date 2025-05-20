/*
|-------------------------------------------------------------------------------
| Development config                      https://maizzle.com/docs/environments
|-------------------------------------------------------------------------------
|
| This is the base configuration that Maizzle will use when you run commands
| like `npm run build` or `npm run dev`. Additional config files will
| inherit these settings, and can override them when necessary.
|
*/

/** @type {import('@maizzle/framework').Config} */
export default {
  build: {
    transformers: {
      baseURL: {
        url: 'https://mgck.ink/uploads/',
        tags: {
          img: { src: true },
        },
      },
    },
    content: ['templates/**/*.html'],
    static: {
      source: ['images/**/*.*'],
      destination: 'images',
    },
  },
};
