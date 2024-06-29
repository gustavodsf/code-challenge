const fs = require('fs');
const path = require('path');

function directoryToTree(rootDir, depth) {
  // Helper function to get the size of a file or directory
  function getSize(filePath) {
    const stats = fs.statSync(filePath);
    if (stats.isDirectory()) {
      const files = fs.readdirSync(filePath);
      return files.reduce((total, file) => {
        return total + getSize(path.join(filePath, file));
      }, 0);
    } else {
      return stats.size;
    }
  }

  const stack = [{ dir: rootDir, depth: 0 }];
  const root = {
    path: rootDir,
    name: path.basename(rootDir),
    type: 'dir',
    size: getSize(rootDir),
    children: []
  };
  const nodes = { '': root };

  while (stack.length > 0) {
    const { dir, depth: currentDepth } = stack.pop();
    const parentNode = nodes[path.relative(rootDir, dir)];

    if (currentDepth < depth) {
      const files = fs.readdirSync(dir);
      for (const file of files) {
        const filePath = path.join(dir, file);
        const stats = fs.statSync(filePath);
        const relativePath = path.relative(rootDir, filePath);
        const node = {
          name: path.basename(filePath),
          path: filePath,
          type: stats.isDirectory() ? 'dir' : 'file',
          size: getSize(filePath),
          children: stats.isDirectory() ? [] : undefined
        };

        parentNode.children.push(node);
        if (stats.isDirectory()) {
          stack.push({ dir: filePath, depth: currentDepth + 1 });
          nodes[relativePath] = node;
        }
      }
    }
  }

  return root;
}

// Example usage
module.exports = directoryToTree;