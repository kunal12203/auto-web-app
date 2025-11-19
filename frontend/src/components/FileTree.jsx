import { useState } from 'react'
import './FileTree.css'

function FileTree({ files, selectedFile, onSelectFile }) {
  const [expandedFolders, setExpandedFolders] = useState(new Set(['root']))

  const buildTree = (files) => {
    const tree = {}
    Object.keys(files).forEach(path => {
      const parts = path.split('/')
      let current = tree
      parts.forEach((part, index) => {
        if (!current[part]) current[part] = index === parts.length - 1 ? null : {}
        if (index < parts.length - 1) current = current[part]
      })
    })
    return tree
  }

  const toggleFolder = (path) => {
    const newExpanded = new Set(expandedFolders)
    newExpanded.has(path) ? newExpanded.delete(path) : newExpanded.add(path)
    setExpandedFolders(newExpanded)
  }

  const getIcon = (name, isFolder, isOpen) => {
    if (isFolder) return isOpen ? '📂' : '📁'
    if (name.endsWith('.html')) return '🌐'
    if (name.endsWith('.css')) return '🎨'
    if (name.endsWith('.js') || name.endsWith('.jsx')) return '📜'
    if (name.endsWith('.json')) return '⚙️'
    return '📄'
  }

  const renderTree = (tree, path = '', level = 0) => {
    return Object.keys(tree).sort().map(key => {
      const currentPath = path ? `${path}/${key}` : key
      const isFolder = tree[key] !== null
      const isExpanded = expandedFolders.has(currentPath)
      const isSelected = selectedFile === currentPath

      return (
        <div key={currentPath} className="tree-node">
          <div 
            className={`node-row ${isSelected ? 'selected' : ''} ${isFolder ? 'folder' : 'file'}`}
            style={{ paddingLeft: `${level * 20 + 12}px` }}
            onClick={() => isFolder ? toggleFolder(currentPath) : onSelectFile(currentPath)}
          >
            <span className="node-icon">{getIcon(key, isFolder, isExpanded)}</span>
            <span className="node-name">{key}</span>
          </div>
          {isFolder && isExpanded && (
            <div className="node-children">
              {renderTree(tree[key], currentPath, level + 1)}
            </div>
          )}
        </div>
      )
    })
  }

  return (
    <div className="file-tree-container">
      <div className="tree-header">PROJECT EXPLORER</div>
      <div className="tree-content">
        {renderTree(buildTree(files))}
      </div>
    </div>
  )
}

export default FileTree