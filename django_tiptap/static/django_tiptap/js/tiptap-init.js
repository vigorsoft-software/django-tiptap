document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('[data-tiptap]').forEach(function (el) {
    const editor = new window.tiptap.Editor({
      element: el,
      extensions: [window.tiptapStarterKit.StarterKit],
    })
  })
})
