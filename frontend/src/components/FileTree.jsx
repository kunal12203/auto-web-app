import { useState } from 'react'
import './FileTree.css'

function FileTree({ files, selectedFile, onSelectFile }) {
  const [expandedFolders, setExpandedFolders] = useState(new Set(['root']))

  // Build tree structure from flat file paths
  const buildTree = (files) => {
    const tree = {}

    Object.keys(files).forEach(path => {
      const parts = path.split('/')
      let current = tree

      parts.forEach((part, index) => {
        if (!current[part]) {
          current[part] = index === parts.length - 1 ? null : {}
        }
        if (index < parts.length - 1) {
          current = current[part]
        }
      })
    })

    return tree
  }

  const toggleFolder = (path) => {
    const newExpanded = new Set(expandedFolders)
    if (newExpanded.has(path)) {
      newExpanded.delete(path)
    } else {
      newExpanded.add(path)
    }
    setExpandedFolders(newExpanded)
  }

  const getFileIcon = (filename) => {
    if (filename.endsWith('.jsx') || filename.endsWith('.js')) {
      return '📜'
    } else if (filename.endsWith('.css')) {
      return '🎨'
    } else if (filename.endsWith('.html')) {
      return '📄'
    } else if (filename.endsWith('.json')) {
      return '📋'
    } else if (filename.endsWith('.md')) {
      return '📝'
    } else if (filename === 'Dockerfile' || filename === 'docker-compose.yml') {
      return '🐳'
    } else if (filename === '.env' || filename.endsWith('.env.example')) {
      return '🔐'
    } else if (filename === '.gitignore') {
      return '🚫'
    } else {
      return '📄'
    }
  }

  const renderTree = (tree, path = '', level = 0) => {
    return Object.keys(tree).sort().map(key => {
      const currentPath = path ? `${path}/${key}` : key
      const isFolder = tree[key] !== null
      const isExpanded = expandedFolders.has(currentPath)
      const isSelected = selectedFile === currentPath

      if (isFolder) {
        return (
          <div key={currentPath} className="folder-item">
            <div
              className={`folder-header ${isExpanded ? 'expanded' : ''}`}
              style={{ paddingLeft: `${level * 16}px` }}
              onClick={() => toggleFolder(currentPath)}
            >
              <span className="folder-icon">{isExpanded ? '📂' : '📁'}</span>
              <span className="folder-name">{key}</span>
            </div>
            {isExpanded && (
              <div className="folder-contents">
                {renderTree(tree[key], currentPath, level + 1)}
              </div>
            )}
          </div>
        )
      } else {
        return (
          <div
            key={currentPath}
            className={`file-item ${isSelected ? 'selected' : ''}`}
            style={{ paddingLeft: `${(level + 1) * 16}px` }}
            onClick={() => onSelectFile(currentPath)}
          >
            <span className="file-icon">{getFileIcon(key)}</span>
            <span className="file-name">{key}</span>
          </div>
        )
      }
    })
  }

  const tree = buildTree(files)

  return (
    <div className="file-tree">
      <div className="file-tree-header">
        <span className="folder-icon">📁</span>
        <span>Project Files</span>
      </div>
      <div className="file-tree-content">
        {renderTree(tree)}
      </div>
      <div className="file-tree-footer">
        {Object.keys(files).length} files
      </div>
    </div>
  )
}

export default FileTree
