/**
 * Local Storage utilities for managing chat threads
 * This will be replaced with database storage in the future
 */

const STORAGE_PREFIX = 'chat_thread_';
const THREADS_LIST_KEY = 'chat_threads_list';
const CURRENT_THREAD_KEY = 'current_thread_id';

/**
 * Generate a unique thread ID
 */
export const generateThreadId = () => {
  return `thread_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
};

/**
 * Save a chat thread to local storage
 */
export const saveChatThread = (threadId, threadData) => {
  try {
    const key = STORAGE_PREFIX + threadId;
    localStorage.setItem(key, JSON.stringify(threadData));

    // Update threads list
    const threadsList = getThreadsList();
    if (!threadsList.find(t => t.id === threadId)) {
      threadsList.unshift({
        id: threadId,
        name: threadData.name || 'Untitled Chat',
        createdAt: threadData.createdAt || new Date().toISOString(),
        updatedAt: new Date().toISOString(),
        messageCount: threadData.messages?.length || 0
      });
      localStorage.setItem(THREADS_LIST_KEY, JSON.stringify(threadsList));
    } else {
      // Update existing thread metadata
      const updatedList = threadsList.map(t =>
        t.id === threadId
          ? { ...t, updatedAt: new Date().toISOString(), messageCount: threadData.messages?.length || 0 }
          : t
      );
      localStorage.setItem(THREADS_LIST_KEY, JSON.stringify(updatedList));
    }

    return true;
  } catch (error) {
    console.error('Error saving chat thread:', error);
    return false;
  }
};

/**
 * Load a chat thread from local storage
 */
export const loadChatThread = (threadId) => {
  try {
    const key = STORAGE_PREFIX + threadId;
    const data = localStorage.getItem(key);
    return data ? JSON.parse(data) : null;
  } catch (error) {
    console.error('Error loading chat thread:', error);
    return null;
  }
};

/**
 * Get list of all chat threads
 */
export const getThreadsList = () => {
  try {
    const data = localStorage.getItem(THREADS_LIST_KEY);
    return data ? JSON.parse(data) : [];
  } catch (error) {
    console.error('Error getting threads list:', error);
    return [];
  }
};

/**
 * Delete a chat thread
 */
export const deleteChatThread = (threadId) => {
  try {
    const key = STORAGE_PREFIX + threadId;
    localStorage.removeItem(key);

    // Update threads list
    const threadsList = getThreadsList();
    const updatedList = threadsList.filter(t => t.id !== threadId);
    localStorage.setItem(THREADS_LIST_KEY, JSON.stringify(updatedList));

    return true;
  } catch (error) {
    console.error('Error deleting chat thread:', error);
    return false;
  }
};

/**
 * Set current active thread
 */
export const setCurrentThread = (threadId) => {
  localStorage.setItem(CURRENT_THREAD_KEY, threadId);
};

/**
 * Get current active thread ID
 */
export const getCurrentThread = () => {
  return localStorage.getItem(CURRENT_THREAD_KEY);
};

/**
 * Auto-save current thread state
 */
export const autoSaveThread = (threadId, messages, projectData) => {
  const threadData = {
    id: threadId,
    name: projectData.projectName || 'Untitled Chat',
    messages: messages,
    projectFiles: projectData.projectFiles,
    projectName: projectData.projectName,
    projectType: projectData.projectType,
    paymentGateway: projectData.paymentGateway,
    projectSessionId: projectData.projectSessionId,
    createdAt: getCurrentThread() === threadId ? loadChatThread(threadId)?.createdAt : new Date().toISOString(),
    updatedAt: new Date().toISOString()
  };

  return saveChatThread(threadId, threadData);
};
